from .annSav import AnnSav


# The class XmlSav is inheriting from the class AnnSav.
class XmlSav(AnnSav):
    
    def __init__(self, target_file_path: str, ann_aug, data_name: str) -> None:
        super().__init__(target_file_path, ann_aug, data_name)
        self.dataSaver()
        
    def dataSaver(self):
        
        with open(self.target_file_path + '\\' + self.data_name + '.xml', 'w') as f:
            
            f.write(str(self.ann_aug))