from typing import IO
from .annOp import AnnotationOpener


# The XmlFileOpener class is a subclass of AnnotationOpener used for opening XML files.
class XmlFileOpener(AnnotationOpener):

    def __init__(self, open_file_name: str) -> None:
        """
        This is a constructor function that initializes an object with a given file name, sets the file
        extension to ".xml", and opens the data from the file.
        
        :param open_file_name: The parameter `open_file_name` is a string that represents the name or path
        of the file that needs to be opened. It is used in the `__init__` method to initialize the object
        with the specified file
        :type open_file_name: str
        """

        super().__init__(open_file_name)
        self.ext = ".xml"
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
                xml_data = f.read()
            return xml_data
        
        except Exception as e:
            print(f"An error occurred while opening file {self.data_name}: {e}")
            return None
        
    def __repr__(self) -> str:
        """
        This function is used to return a string representation of an object.
        """
        return "xml"