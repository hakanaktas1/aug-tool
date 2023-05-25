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
                                        y_shift=y_shift).image_aug
                
    
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

                    
                elif self.ann.ext == ".txt":
                    
                    ann_aug = dataAugmentor.TxtAug(
                                                annotate= self.ann.data,
                                                x_shift=x_shift,
                                                y_shift=y_shift,
                                                width=aug_image.width,
                                                height=aug_image.height).aug_anotate
                    
                    dataSaver.TxtSav(target_file_path = self.target_file_name,
                                     ann_aug=ann_aug,
                                    data_name=data_name)
                else:
                    logging.exception('There is no annonation file!') 
                    
    
        
        
        self.labeled_path = None
        self.image_path = None

    
    @staticmethod
    def create_dest_folder(target):

        if not os.path.exists(target):
            try:
                os.mkdir(target)
            except:
                logging.exception('Could not create folder! ')
        else:
            logging.exception('There is already folder!')
            
    @staticmethod
    def create_list_of_data(open_data_path) -> list:
        """
        The function "create_list_of_data" takes a file path as input and returns a list of data.
        
        :param open_data_path: The parameter `open_data_path` is expected to be a string representing the
        file path of a data file that needs to be opened and read. The function `create_list_of_data` will
        read the data from this file and return it as a list
        """
        try:
            raise Exception("foto asdasd")
            image_extensions = ['.jpg', '.jpeg', '.png']
            image_files = []

            for file in os.listdir(open_data_path):
                
                if os.path.isfile(os.path.join(open_data_path, file)):
                    
                    ext = os.path.splitext(file)[1].lower()
                    if ext in image_extensions:
                        
                        image_files.append(os.path.join(open_data_path, file))

            return image_files
        except:
            logging.exception('Deneme Okta kardesim icin')
    
    
    @property
    def target_file_name(self) -> str:
        """
        This function returns a string representing the target file name.
        """
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
    
    number_of_aug = 2,
    
    Factory(open_data_path=open_file_name,
            save_file_name=save_file_name,
            number_of_aug=number_of_aug,
            x_shift=33,
            y_shift=33)