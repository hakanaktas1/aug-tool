from .annAug import AnnAug

class XmlAug(AnnAug):
    def __init__(self, name: str, annotate, x_shift: int, y_shift: int) -> None:
        super().__init__(name, annotate, x_shift, y_shift)

    def create_new_cords(self):
        pass   

    def write_new_cords(self):
        pass