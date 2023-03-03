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


# calculate power for SLIM design
print('300K -> 50K (SS)')
wire = CoaxWiring('034-SS-SS', 0.3)
wire_power = wire.power(40, 290)
print('Loading per wire: {:.2e} W'.format(wire_power))
print('Loading for 9 wires: {:.2e} W\n'.format(wire_power*9))

print('50K -> 4K (SS)')
wire = CoaxWiring('034-SS-SS', 0.5)
wire_power = wire.power(3.2, 40)
print('Loading per wire: {:.2e} W'.format(wire_power))
print('Loading for 9 wires: {:.2e} W\n'.format(wire_power*9))

print('4K -> 1K (SS)')
wire = CoaxWiring('034-SS-SS', 0.3)
wire_power = wire.power(0.8, 3.2)
print('Loading per wire: {:.2e} W'.format(wire_power))
print('Loading for 9 wires: {:.2e} W\n'.format(wire_power*9))

print('1K -> 100mK (SS)')
wire = CoaxWiring('034-SS-SS', 0.5)
wire_power = wire.power(0.1, 0.8)
print('Loading per wire: {:.2e} W'.format(wire_power))
print('Loading for 9 wires: {:.2e} W\n'.format(wire_power*9))

print('100mK -> 1K (NbTi)')
wire = CoaxWiring('034-NbTi-NbTi', 0.5)
wire_power = wire.power(0.1, 0.8)
print('Loading per wire: {:.2e} W'.format(wire_power))
print('Loading for 9 wires: {:.2e} W\n'.format(wire_power*9))

print('1K ->4K (NbTi)')
wire = CoaxWiring('034-NbTi-NbTi', 0.3)
wire_power = wire.power(0.8, 3.2)
print('Loading per wire: {:.2e} W'.format(wire_power))
print('Loading for 9 wires: {:.2e} W\n'.format(wire_power*9))

print('4K -> 50K (SS) (update this to silver plated!!)')
wire = CoaxWiring('034-SS-SS', 0.5)
wire_power = wire.power(3.2, 40)
print('Loading per wire: {:.2e} W'.format(wire_power))
print('Loading for 9 wires: {:.2e} W\n'.format(wire_power*9))

print('50K -> 300K (SS)')
wire = CoaxWiring('034-SS-SS', 0.3)
wire_power = wire.power(40, 290)
print('Loading per wire: {:.2e} W'.format(wire_power))
print('Loading for 9 wires: {:.2e} W\n'.format(wire_power*9))