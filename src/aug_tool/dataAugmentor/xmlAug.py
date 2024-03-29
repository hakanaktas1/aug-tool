from .annAug import AnnAug

import random

class XmlAug(AnnAug):
    def __init__(self, name: str, annotate, x_shift: int, y_shift: int, random_x:int, random_y:int) -> None:
        super().__init__(name, annotate, x_shift, y_shift)
        self.name = name
        self.annotate = annotate
        self.x_min_new = []
        self.x_max_new = []
        self.y_min_new = []
        self.y_max_new = []
        self.x_shift = x_shift
        self.y_shift = y_shift
        self.random_x = random_x
        self.random_y = random_y
        self.create_new_cords()
        self.write_new_cords()
        

    def create_new_cords(self):
        
        random_noise  = random.randint(-2, 2)
        
        for i in self.annotate.find_all('xmin'):
            self.x_min_new.append(int(i.text) + (self.random_x - int(self.x_shift)) + random_noise)
        for i in self.annotate.find_all('xmax'):
            self.x_max_new.append(int(i.text) + (self.random_x - int(self.x_shift)) + random_noise)
        for i in self.annotate.find_all('ymin'):
            self.y_min_new.append(int(i.text) + (self.random_y - int(self.y_shift)) + random_noise)
        for i in self.annotate.find_all('ymax'):
            self.y_max_new.append(int(i.text) + (self.random_y - int(self.y_shift)) + random_noise)


        # for i in self.annotate.find_all('xmin'):
        #     self.x_min_new.append(int(i.text) + (self.random_x - int(self.x_shift)))
        # for i in self.annotate.find_all('xmax'):
        #     self.x_max_new.append(int(i.text) + (self.random_x - int(self.x_shift)))
        # for i in self.annotate.find_all('ymin'):
        #     self.y_min_new.append(int(i.text) + (self.random_y - int(self.y_shift)))
        # for i in self.annotate.find_all('ymax'):
        #     self.y_max_new.append(int(i.text) + (self.random_y - int(self.y_shift)))

    def write_new_cords(self):
        
        for count in range(len(self.annotate.find_all('xmin'))):
            self.annotate.find_all('xmin')[count].string = str(self.x_min_new[count])

        for count in range(len(self.annotate.find_all('xmax'))):
            self.annotate.find_all('xmax')[count].string = str(self.x_max_new[count])

        for count in range(len(self.annotate.find_all('ymin'))):
            self.annotate.find_all('ymin')[count].string = str(self.y_min_new[count])

        for count in range(len(self.annotate.find_all('ymax'))):
            self.annotate.find_all('ymax')[count].string = str(self.y_max_new[count])

        self.annotate.find_all('filename')[0].string = self.name + ".jpg"
        self.annotate.find_all('path')[0].string =  self.name + ".jpg"
    