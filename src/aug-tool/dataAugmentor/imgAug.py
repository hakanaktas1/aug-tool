from .dataAug import DataAug

class ImgAug(DataAug):
    
    rotate_rate = None
    
    def __init__(self, name: str, image, annotate, x_shift: int, y_shift: int, brigness: bool, contrast:bool, sharpen: bool) -> None:
        super().__init__(name, image, annotate, x_shift, y_shift)
        self.image = image    
        self.brigness = brigness
        self.contrast = contrast
        self.sharpen = sharpen  

    def carve_out(self):
        pass
    def apply_adj(self):
        pass    
