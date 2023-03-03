from .thermal import conductivity_integral
from .heat_sources import HeatSource
import yaml
import os
import numpy as np

with open(os.path.join(os.path.dirname(__file__),
            'data/wiring/coax_params.yaml'), 'r') as f:
    coax_data = yaml.safe_load(f)

class CoaxWiring(HeatSource):
    def __init__(self, coax_type, length):
        self.coax_type = coax_type
        self.coax_params = coax_data[coax_type]
        self.length = length

    def power(self, T_low, T_high):
        # compute conductivity integrals
        # outer conductor
        outer_integral = conductivity_integral(self.coax_params['outer material'],
                                                         T_low, T_high)
        power_outer = outer_integral * \
                      np.pi * ((self.coax_params['outer diameter']/2)**2 - (self.coax_params['dielectric diameter']/2)**2) / \
                      self.length

        # inner conductor
        inner_integral = conductivity_integral(self.coax_params['inner material'],
                                                         T_low, T_high)
        power_inner = inner_integral * \
                      np.pi * ((self.coax_params['inner diameter']/2)**2) / \
                      self.length
        
        # dielectric
        dielectric_integral = conductivity_integral(self.coax_params['dielectric material'],
                                                         T_low, T_high)
        power_dielectric = dielectric_integral * \
                      np.pi * ((self.coax_params['dielectric diameter']/2)**2 - (self.coax_params['inner diameter']/2)**2) / \
                      self.length
        
        power_total = power_outer + power_inner + power_dielectric
        return power_total