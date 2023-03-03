import numpy as np
from abc import ABC, abstractmethod
from thermal import conductivity_integral
import yaml
import os

class HeatSource(ABC):
    '''
    Abstract base class for a heat source on a stage. Derived classes are 
    meant to correspond to different types of thermal loads, which vary based
    on material properties.
    '''
    @abstractmethod
    def __init__(self):
        pass

    @abstractmethod
    def power(self):
        pass
    
class CoaxWiring(HeatSource):
    def __init__(self, coax_type):
        self.coax_type = coax_type
        with open(os.path.join(os.path.dirname(__file__),
                  'data/wiring/coax_params.yaml'), 'r') as f:
            self.coax_data = yaml.safe_load(f)

    def power(self, T_low, T_high):
        cond_integral = conductivity_integral(self.coax_type, T_low, T_high)
        return cond_integral * (T_high - T_low)