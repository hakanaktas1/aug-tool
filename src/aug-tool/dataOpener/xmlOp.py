from typing import IO
from .annOp import AnnotationOpener


# The TxtFileOpener class is a subclass of AnnotationOpener and is used for opening and reading text files.
class TxtFileOpener(AnnotationOpener):
 
    def __init__(self, open_file_name: str) -> None:
        """
        This is the constructor of a class that takes a file name as input, sets the file extension to
        ".txt", and opens the data from the file.
        
        :param open_file_name: The parameter `open_file_name` is a string that represents the name or path
        of the file that will be opened and read by the program. It is used in the `__init__` method to
        initialize the parent class and to set the file extension to `.txt`. The `open_data`
        :type open_file_name: str
        """
        super().__init__(open_file_name)
        self.ext = ".txt"
        self.data = self.open_data()
        
    @property    
    def data_name(self):

        return self.open_file_name[:-4] + self.ext
        
    def open_data(self) -> IO:
        """
        This function returns an IO object for reading data.
        """
        try:
            with open(self.data_name, self.mode) as f:
                txt_data = f.read()
            return txt_data
        
        except Exception as e:
            print(f"An error occurred while opening file {self.data_name}: {e}")
            return None
        
    def __repr__(self) -> str:
        return super().__repr__()