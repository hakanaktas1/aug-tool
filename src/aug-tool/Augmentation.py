import random
from bs4 import BeautifulSoup
from PIL import Image, ImageEnhance, ImageFilter
from importlib import resources
import io

class Augmentor:

    def __init__(self, image=None, xml=None, data_name=None, shift_x=None, shift_y=None, noise_effect=False, brightness_effect=False, contrast_effect=False, sharpness_effect = False) -> None:
        """
        This function takes in an image, an xml file, a data name, a shift x, a shift y, a noise effect, a
        brightness effect, a contrast effect, and a sharpness effect, and then it applies a random value to
        shift, carves out the image, carves out the xml, applies a noise effect, and applies an adjustment.
        
        :param image: the image file
        :param xml: the xml file that contains the bounding box coordinates
        :param data_name: The name of the image file
        :param shift_x: The amount of pixels to shift the image in the x direction
        :param shift_y: The amount of pixels to shift the image up or down
        :param noise_effect: If True, then the image will be noisy, defaults to False (optional)
        :param brightness_effect: If True, the image will be adjusted to be brighter, defaults to False
        (optional)
        :param contrast_effect: If True, the image will be adjusted for contrast, defaults to False
        (optional)
        :param sharpness_effect: True/False, defaults to False (optional)
        """

        self.image = image
        self.xml = xml
        self.data_name = data_name
        self.shift_x = shift_x
        self.shift_y = shift_y
        self.noise_effect = noise_effect
        self.brightness_effect = brightness_effect
        self.contrast_effect = contrast_effect
        self.sharpness_effect = sharpness_effect

    def augmentor(self):

        self.random_value_to_shift()
        self.carve_out_image()
        self.carve_out_xml()

        if self.noise_effect:
            self.apply_noise_effect()

        self.apply_adjustment()

    def random_value_to_shift(self):
        """
        It takes the shift_x and shift_y values and multiplies them by 2, then it takes a random integer
        between 0 and the product of the shift_x and shift_y values
        """
        self.rand_ratio_x = random.randint(0, int(int(self.shift_x) * 2))
        self.rand_ratio_y = random.randint(0, int(int(self.shift_y) * 2))

    def carve_out_image(self):
        """
        It takes an image and crops it out by a random amount, then pastes it back into the original
        image at a random location
        """

        self.image_aug = self.image.copy()
        self.image_aug = self.image_aug.filter(ImageFilter.BoxBlur(15))

        self.width, self.height = self.image.size
        self.image = self.image.crop((int(self.shift_x), int(self.shift_y),
                            self.width - int(self.shift_x), self.height - int(self.shift_y)))
        # img1 = img1.rotate(5, fillcolor=(1,0,0), expand=False)
        self.image_aug.paste(self.image, (self.rand_ratio_x, self.rand_ratio_y))

    def carve_out_xml(self):
        """
        It takes an XML file, and shifts the coordinates of the bounding boxes in the XML file by a
        random amount
        """
        
        self.xml_file = BeautifulSoup(self.xml, "xml")

        x_min_new = []
        x_max_new = []
        y_min_new = []
        y_max_new = []

        for i in self.xml_file.find_all('xmin'):
            x_min_new.append(int(i.text) + (self.rand_ratio_x - int(self.shift_x)))
        for i in self.xml_file.find_all('xmax'):
            x_max_new.append(int(i.text) + (self.rand_ratio_x - int(self.shift_x)))
        for i in self.xml_file.find_all('ymin'):
            y_min_new.append(int(i.text) + (self.rand_ratio_y - int(self.shift_y)))
        for i in self.xml_file.find_all('ymax'):
            y_max_new.append(int(i.text) + (self.rand_ratio_y - int(self.shift_y)))

        for count in range(len(self.xml_file.find_all('xmin'))):
            self.xml_file.find_all('xmin')[count].string = str(x_min_new[count])

        for count in range(len(self.xml_file.find_all('xmax'))):
            self.xml_file.find_all('xmax')[count].string = str(x_max_new[count])

        for count in range(len(self.xml_file.find_all('ymin'))):
            self.xml_file.find_all('ymin')[count].string = str(y_min_new[count])

        for count in range(len(self.xml_file.find_all('ymax'))):
            self.xml_file.find_all('ymax')[count].string = str(y_max_new[count])

        self.xml_file.find_all('filename')[0].string = self.data_name + ".jpg"
        self.xml_file.find_all('path')[0].string =  self.data_name + ".jpg"

    def apply_noise_effect(self):
        """
        It takes an image and pastes it on top of another image.
        """

        effect1_img = "C:\Users\hakan.aktas\Desktop\deneme\effect\effect_" + str(random.randint(1, 2)) + ".png"
        
        with resources.open_binary('aug-tool', effect1_img) as fp:
            effect_img = fp.read()
        effect_img = Image.open(io.BytesIO(effect_img))

        effect1_img = effect1_img.resize((self.width, self.height))
        self.image_aug.paste(effect1_img, (0, 0), mask=effect1_img)

    def apply_adjustment(self):
        """
        If the user has selected any of the three checkboxes, then randomly select one of the three and
        apply a random brightness factor to it
        """
        queue = []

        if self.contrast_effect:
            queue.append("Contrast")
        if self.brightness_effect:
            queue.append("Brigness")
        if self.contrast_effect:
            queue.append("Sharpness")

        if len(queue) != 0:
            brig_factor = random.uniform(0.2, 2)
            # brig_factor = random.uniform(float(self.ui.doubleSpinBox_Min.decimals()),
            #                              float(self.ui.doubleSpinBox_Max.decimals()))
            lucky_shot = random.randint(0, len(queue) - 1)

            if "Brigness" == queue[lucky_shot]:
                self.image_aug = ImageEnhance.Brightness(self.image_aug)
            elif "Contrast" == queue[lucky_shot]:
                self.image_aug = ImageEnhance.Contrast(self.image_aug)
            elif "Sharpness" == queue[lucky_shot]:
                self.image_aug = ImageEnhance.Sharpness(self.image_aug)

            self.image_aug = self.image_aug.enhance(brig_factor)
        else:
            pass


