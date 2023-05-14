from .dataSav import DataSaver

# The ImgSav class is a subclass of DataSaver.
class ImgSav(DataSaver):
   
    def __init__(self, target_file_path: str, img_aug, data_name: str) -> None:
        super().__init__(target_file_path, img_aug, data_name)
        self.dataSaver()
   
    def dataSaver(self):
        self.img_aug.save(self.target_file_path + '\\' + self.data_name + ".jpg")