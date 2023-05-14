from .dataOpener.dataOp import DataOpener
from .dataAugmentor.dataAug import DataAug
from .dataSaver.dataSav import DataSaver
import os
from os.path import join
import logging
import glob


class Factory(object):
    def __init__(self, open_data_path:str, save_file_name:str) -> None:
        self.open_data_path = open_data_path
        self.save_file_name = save_file_name
        
        self.create_dest_folder(self.target_file_name)
        
        
        self.labeled_path = None
        self.image_path = None
        pass
    
    @staticmethod
    def create_dest_folder(target):
        try:
            os.mkdir(target)
        except:
            logging.exception('')
            
    @staticmethod
    def create_list_of_data(open_data_path) -> list:
        try:
            files = []
            for ext in ('*.jpg', '*.png', '*.jpeg'):
                files.extend(glob(join(open_data_path, ext)))  
                return files  
        except:
            logging.exception('')
            
    @property
    def target_file_name(self) -> str:
        return str(self.save_file_name) + "/aug_" + str(self.open_data_path.split("\\")[-1])
    


    def find_ext_label(self):
        pass