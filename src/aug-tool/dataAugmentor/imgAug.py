from .dataAug import DataAug
import random
from PIL import ImageEnhance, ImageFilter

class ImgAug(DataAug):
    
    rotate_rate = None
    
    def __init__(self, image, x_shift: int, y_shift: int, contrast:bool = False, brigness:bool = False, sharpen:bool = False ) -> None:
        super().__init__(None, image, None, x_shift, y_shift)
        self.contrast = contrast
        self.brigness = brigness
        self.sharpen = sharpen
        self.aug_image = None   
        self.carve_out()
        self.apply_adj()
        


        
    def carve_out(self):
        
        image_aug = self.image
        image_aug = image_aug.filter(ImageFilter.BoxBlur(5))

        width, height = self.image.size
        
        self.image = self.image.crop((int(self.x_shift), int(self.y_shift),
                            width - int(self.x_shift), height - int(self.y_shift)))
        # img1 = img1.rotate(5, fillcolor=(1,0,0), expand=False)

        image_aug.paste(self.image, (int(self.get_random_x), int(self.get_random_y)))
    
    def apply_adj(self):
        
        queue = []

        if self.contrast:
            queue.append("Contrast")
        if self.brigness:
            queue.append("Brigness")
        if self.sharpen:
            queue.append("Sharpness")

        if len(queue) != 0:
            
            brig_factor = random.uniform(0.2, 2)
            lucky_shot = random.randint(0, len(queue) - 1)

            if "Brigness" == queue[lucky_shot]:
                self.image = ImageEnhance.Brightness(self.image)
            elif "Contrast" == queue[lucky_shot]:
                self.image = ImageEnhance.Contrast(self.image)
            elif "Sharpness" == queue[lucky_shot]:
                self.image = ImageEnhance.Sharpness(self.image)

            self.image = self.image.enhance(brig_factor)
        else:
            pass
