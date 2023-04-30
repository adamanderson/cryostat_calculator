from cryostat_calculator.wiring import CoaxWiring
import numpy as np
import matplotlib.pyplot as plt

stage_names = ['RT', '50K', '4K', 'still', 'CP', 'MXC']
T_stage = [240, 35, 2.85, 0.882, 0.082, 0.06]
cable_lengths = [0.2, 0.29, 0.25, 0.17, 0.14]

# reproducing Figure 1 from:
# Krinner, et al. EPJQuantumTechnology (2019) 6:2 https://doi.org/10.1140/epjqt/s40507-019-0072-0
print('Checking calculations from Fig. 1 of Krinner, et al. (2019):')
wire_power = {'086-NbTi-NbTi':[],
              '086-SS-SS':[]}
for cable_type in wire_power:
    for jstage in range(len(T_stage)-1):
        nbti_wire = CoaxWiring(cable_type, cable_lengths[jstage])
        wire_power[cable_type].append(nbti_wire.power(T_stage[jstage+1], T_stage[jstage]))
        print('{}: {:.2e} W'.format(stage_names[jstage+1], wire_power[cable_type][-1]))
print()

for jtype, cable_type in enumerate(list(wire_power.keys())):
    x = np.arange(len(wire_power[cable_type])) 
    plt.bar(x+0.2*jtype, wire_power[cable_type], width=0.2,
            label=cable_type)
plt.gca().set_yscale('log')
plt.gca().set_xticks(x)
plt.gca().set_xticklabels(stage_names[1:])
plt.ylabel('Power load [W]')
plt.legend()
plt.title('Reproducing Fig. 1 of Krinner, et al.')
plt.tight_layout()
plt.savefig('krinner_figure_test.png', dpi=200)

# SLIM cryostat wiring parameters
Tstage = [290, 45, 3.3, 0.7, 0.1, 0.7, 3.3, 45, 290]
cable_type = ['034-SS-SS', '034-SS-SS', '034-SS-SS', '034-SS-SS',
              '034-NbTi-NbTi', '034-NbTi-NbTi', '034-SS-SS', '034-SS-SS']
cable_length = [0.3, 0.5, 0.3, 0.5, 0.5, 0.3, 0.5, 0.3]

for jcable in np.arange(len(cable_type)):
    # calculate power for SLIM design
    print('{}K -> {}K ({}-m length {})'.format(Tstage[jcable], Tstage[jcable+1], cable_length[jcable], cable_type[jcable]))
    wire = CoaxWiring(cable_type[jcable], cable_length[jcable])
    wire_power = wire.power(np.min(Tstage[jcable:(jcable+2)]),
                            np.max(Tstage[jcable:(jcable+2)]))
    print('Loading per wire: {:.2e} W'.format(wire_power))
    print('Loading for 9 wires: {:.2e} W\n'.format(wire_power*9))