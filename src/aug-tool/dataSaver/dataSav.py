from PIL import Image
from abc import ABC, abstractmethod
from typing import IO


# The class DataSaver is defined as an abstract base class (ABC).
class DataSaver(ABC):
    
    def __init__(self, target_file_path:str, img_aug, ann_aug, data_name:str) -> None:
        self.target_file_path = target_file_path
        self.img_aug = img_aug
        self.ann_aug = ann_aug
        self.data_name = data_name
        
    @abstractmethod
    def dataSaver(self):
        pass