import numpy as np
from abc import ABC, abstractmethod

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
    
