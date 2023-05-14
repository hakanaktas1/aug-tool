from .dataSav import DataSaver


# The AnnSav class is a subclass of DataSaver.
class AnnSav(DataSaver):
    
    def __init__(self, target_file_path: str, ann_aug, data_name: str) -> None:
        super().__init__(target_file_path, ann_aug, data_name)
    
    def dataSaver(self):
        pass