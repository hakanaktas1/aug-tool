import dataAugmentor
import dataOpener
import dataSaver
import os
from os.path import join, exists
import logging
import glob


class Factory(object):
    def __init__(self, open_data_path:str, save_file_name:str, number_of_aug:int, x_shift:int, y_shift:int) -> None:
        self.open_data_path = open_data_path
        self.save_file_name = save_file_name
        self.ann = None
        self.img = None
        
        
        self.create_dest_folder(self.target_file_name)
        
        for data_path in self.create_list_of_data(open_data_path = open_data_path):
            
            self.label_factory(data_path[:-4])
            self.image_factory(data_path)
            
            for num in range(number_of_aug):
                
                data_name = data_path.split("\\")[-1][:-4] + "_aug" + str(num + 1)
                
                aug_image = dataAugmentor.ImgAug(image=self.img,
                                        x_shift=x_shift,
                                        y_shift=y_shift).aug_image
                
    
                dataSaver.ImgSav(target_file_path = self.target_file_name,
                                 img_aug = aug_image,
                                 data_name=data_name)
                
                if self.ann.ext == ".xml":
                    
                    ann_aug = dataAugmentor.XmlAug(name=data_name,
                                                annotate= self.ann.data,
                                                x_shift=x_shift,
                                                y_shift=y_shift)
                    
                    dataSaver.XmlSav(target_file_path = self.target_file_name,
                                                                ann_aug=ann_aug.annotate,
                                                                data_name=data_name)

                    
                elif self.ann == "txt":
                    dataSaver.TxtSav(target_file_path = self.target_file_name,
                                    ann_aug=dataAugmentor.TxtAug(name=data_name,
                                                                annotate= self.ann,
                                                                x_shift=x_shift,
                                                                y_shift=y_shift),
                                    data_name=data_name)
                else:
                    logging.exception('There is no annonation file!')
    
        
        
        self.labeled_path = None
        self.image_path = None

    
    @staticmethod
    def create_dest_folder(target):
        try:
            os.mkdir(target)
        except:
            logging.exception('there is a folder ')
            
    @staticmethod
    def create_list_of_data(open_data_path) -> list:
        try:
  
            image_extensions = ['.jpg', '.jpeg', '.png']
            image_files = []

            for file in os.listdir(open_data_path):
                if os.path.isfile(os.path.join(open_data_path, file)):
                    ext = os.path.splitext(file)[1].lower()
                    if ext in image_extensions:
                        image_files.append(os.path.join(open_data_path, file))

            return image_files
        except:
            logging.exception('')
            
    @property
    def target_file_name(self) -> str:
        return str(self.save_file_name) + "/aug_" + str(self.open_data_path.split("\\")[-1])
    
    def label_factory(self, path:str):
        
        if os.path.exists(path + ".xml"):
            self.ann = dataOpener.XmlFileOpener(path + ".xml")

        elif os.path.exists(path + ".txt"):
            self.ann = dataOpener.TxtFileOpener(path + ".txt")
       
        else:
            logging.exception('There is no any annotation file that has ext such as .xml or .txt in this directory')
            
    def image_factory(self, path:str):
        try:
            self.img = dataOpener.ImgOpener(path).data
        except:
            logging.exception('Could not open image file. (Check its extension.)')
        
        
        
  
            
if __name__ == '__main__':
    
    open_file_name = r"C:\Users\hakan.aktas\Desktop\save\animal1"

    save_file_name = r"C:\Users\hakan.aktas\Desktop\save\animal2"
    number_of_aug = 5
    
    Factory(open_data_path=open_file_name,
            save_file_name=save_file_name,
            number_of_aug=number_of_aug,
            x_shift=15,
            y_shift=15)