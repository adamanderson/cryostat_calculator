import numpy as np
from glob import glob
import os
from scipy.interpolate import interp1d
from scipy.integrate import simpson

# load and interpolate thermal conductivity data
thermal_conductivity_data = {}
for fname in glob(os.path.join(os.path.dirname(__file__),
                  'data/conductivity/*csv')):
    material = os.path.splitext(os.path.basename(fname))[0]
    thermal_conductivity_data[material] = np.loadtxt(fname, delimiter=',')
thermal_conductivity_interp_funcs = {material:
                                     interp1d(thermal_conductivity_data[material][:,0],
                                              thermal_conductivity_data[material][:,1], kind='cubic')
                                     for material in thermal_conductivity_data}

# calculate thermal conductivity integrals
conductivity_integral_interp_funcs = {}
for material in thermal_conductivity_interp_funcs:
    finterp = thermal_conductivity_interp_funcs[material]
    T_min = np.min(finterp.x)
    T_max = np.max(finterp.x)
    T_of_integral = np.logspace(np.log10(T_min), np.log10(T_max))
    intergral_interp = []
    for T in T_of_integral[1:]:
        T_integrand = np.logspace(np.log10(T_min), np.log10(T - 1e-6))
        intergral_interp.append(simpson(finterp(T_integrand), T_integrand))
    conductivity_integral_interp_funcs[material] = interp1d(T_of_integral[1:], intergral_interp, kind='cubic')

def thermal_conductivity(material, T):
    return thermal_conductivity_interp_funcs[material](T)

def conductivity_integral(material, T_low, T_high):
    return conductivity_integral_interp_funcs[material](T_high) - \
           conductivity_integral_interp_funcs[material](T_low)