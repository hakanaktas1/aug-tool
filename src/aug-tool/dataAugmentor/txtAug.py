from .annAug import AnnAug

class TxtAug(AnnAug):
    def __init__(self, annotate, x_shift: int, y_shift: int, width,height) -> None:
        super().__init__(None, annotate, x_shift, y_shift)
        self.aug_anotate = self.create_new_cords(width, height)
        
    def create_new_cords(self, width, height):
        lines = self.annotate.readlines() 
        self.annotate.seek(0)
        aug_values = []
        for line in lines:
    
            values = line.strip().split()

            aug_x_center = float(values[1]) + (self.get_random_x - int(self.x_shift))/width
            aug_y_center = float(values[2]) + (self.get_random_y - int(self.y_shift))/height
            values[1] = str(aug_x_center)
            values[2] = str(aug_y_center)

            aug_line = " ".join(values)
            
            aug_values.append(aug_line)

        return aug_values
        
    def write_new_cords(self):
        pass