from PIL import Image
from abc import ABC, abstractmethod
from typing import IO

# The class DataOpener is defined as an abstract base class (ABC) in Python.
class DataOpener(ABC):
    def __init__(self, open_file_name:str) -> None:
        self.open_file_name = open_file_name
        
    @abstractmethod
    def data_name(self):
        return self.open_file_name[:-4]
    
    @abstractmethod
    def open_data(self):
        pass
    
    def __repr__(self) -> str:
        return "Data information."