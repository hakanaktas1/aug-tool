from PIL import Image
from .dataOp import DataOpener


# The ImgOpener class is a subclass of the DataOpener class in Python.
class ImgOpener(DataOpener):
    
    def __init__(self, open_file_name: str) -> None:
        """
        This is a constructor function that initializes an object with an open file name and opens the data
        in the file.
        
        :param open_file_name: A string representing the name or path of the file to be opened
        :type open_file_name: str
        """
        super().__init__(open_file_name)
        self.data = self.open_data()
        
    @property    
    def data_name(self):
        return self.open_file_name[:-4] + ".jpg"
        
    def open_data(self) -> Image:
        """
        The function "open_data" returns an Image object.
        """
        return Image.open(self.data_name)
    
    def __repr__(self) -> str:
        return super().__repr__()