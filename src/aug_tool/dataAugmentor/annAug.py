from .dataAug import DataAug
from abc import ABC, abstractmethod

class AnnAug(DataAug, ABC):
    
    ran_cord_rate = None
    new_cords = None
    
    def __init__(self, name: str, annotate, x_shift: int, y_shift: int) -> None:
        super().__init__(name, None, annotate, x_shift, y_shift)
        
    @abstractmethod
    def create_new_cords(self):
        pass
    
    @abstractmethod
    def write_new_cords(self):
        pass