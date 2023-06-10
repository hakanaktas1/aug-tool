import random

class DataAug(object):
    def __init__(self, name:str, image, annotate, x_shift:int, y_shift:int) -> None:
        self.name = name
        self.image = image
        self.annotate = annotate
        self.x_shift = x_shift
        self.y_shift = y_shift
        random_x = None
        random_y = None       
        
    @classmethod
    def get_random_x(cls, x_shift):
        cls.random_x = random.randint(0, int(int(x_shift) * 2))
        
    @classmethod
    def get_random_y(cls, y_shift):
        cls.random_y = random.randint(0, int(int(y_shift) * 2))
