import random
import os
# from PyQt5 import QtGui
# from PyQt5.QtWidgets import QFileDialog
import glob
from PIL import Image
from Augmentation import Augmentor


class Loop:
    def loop(self, open_file, save_file, number_of_copy, shift_x, shift_y, random_noise=False,
                 random_brightness=False, random_contrast=False, random_sharpness=False):
        

        os.mkdir(str(save_file) + "/aug_" + str(open_file.split("/")[-1]))

        for images_path in self.list_of_data(open_data=open_file):
            self.data_path = images_path[:-4]
            self.open_data()

            for count in range(int(number_of_copy)):

                self.aug_data_name = images_path.split("\\")[-1][:-4] + "_aug" + str(count + 1)

                aug_data = Augmentor(image=self.pillow_image,
                                     xml=self.xml_data,
                                     data_name=self.aug_data_name,
                                     shift_x=shift_x,
                                     shift_y=shift_y,
                                     noise_effect=random_noise,
                                     brightness_effect=random_brightness,
                                     contrast_effect=random_contrast,
                                     sharpness_effect=random_sharpness)
                aug_data.augmentor()

                self.save_data(aug_image=aug_data.image_aug,
                               aug_xml=aug_data.xml_file,
                               data_name=self.aug_data_name,
                               open_data=open_file,
                               save_data=save_file)

    def open_data(self):
        """
        It opens the image and xml data for the image.
        """

        self.pillow_image = Image.open(self.data_path + ".jpg")
        with open(self.data_path + '.xml', 'r') as f:
            self.xml_data = f.read()
       
    def save_data(self, aug_image, aug_xml, data_name, open_data, save_data):
        """
        It takes the augmented image and the augmented xml file and saves them in the aug_image folder
        
        :param aug_image: The augmented image
        :param aug_xml: the xml file that contains the bounding box information
        :param data_name: The name of the augmented image
        """
        aug_image.save(save_data + "/aug_" + str(open_data.split("/")[-1]) + '/' + data_name + ".jpg")

        with open(save_data + "/aug_" + str(open_data.split("/")[-1]) + '/' + data_name + '.xml', 'w') as f:
            f.write(str(aug_xml))
      


    def list_of_data(self, open_data:str):
        """
        This function opens a file dialog and creates a list of all the .jpg files in the selected
        directory.
        
        :param open_data: A string representing the directory path where the user wants to search for .jpg
        files
        :type open_data: str
        :return: a list of all the .jpg files in the directory selected by the user through a file dialog.
        """
        
        return glob.glob(str(open_data) + "\*.jpg")

    def pil2pixmap(self, im):
        """
        It takes a PIL image and converts it to a QPixmap.
        
        :param im: the image to be converted
        :return: A QPixmap object.
        """

        if im.mode == "RGB":
            r, g, b = im.split()
            im = Image.merge("RGB", (b, g, r))
        elif im.mode == "RGBA":
            r, g, b, a = im.split()
            im = Image.merge("RGBA", (b, g, r, a))
        elif im.mode == "L":
            im = im.convert("RGBA")
        im2 = im.convert("RGBA")
        data = im2.tobytes("raw", "RGBA")
        qim = QtGui.QImage(data, im.size[0], im.size[1], QtGui.QImage.Format_ARGB32)
        pixmap = QtGui.QPixmap.fromImage(qim)
        return pixmap





