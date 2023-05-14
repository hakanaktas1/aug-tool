import random

class DataAug(object):
    def __init__(self, name:str, image, annotate, x_shift:int, y_shift:int) -> None:
        self.name = name
        self.image = image
        self.annotate = annotate
        self.x_shift = x_shift
        self.y_shift = y_shift
        
    @property
    def get_random_x(self):
        return random.randint(0, int(int(self.x_shift) * 2))
    
    @property
    def get_random_y(self):
        return random.randint(0, int(int(self.y_shift) * 2))