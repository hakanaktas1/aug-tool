import random

class DataAug(object):
    def __init__(self, name:str, image, annotate, x_shift:int, y_shift:int) -> None:
        self.name = name
        self.image = image
        self.annotate = annotate
        
    @staticmethod
    def get_random_x(x_shift):
        return random.randint(0, int(int(x_shift) * 2))
    @staticmethod
    def get_random_y(y_shift):
        return random.randint(0, int(int(y_shift) * 2))

