from typing import IO
from .dataOp import DataOpener


# The AnnotationOpener class is a subclass of the DataOpener class in Python.
class AnnotationOpener(DataOpener):
    
    mode = "r"
    
    def __init__(self, open_file_name: str) -> None:
        super().__init__(open_file_name)
    
    def data_name(self):
        return self.open_file_name[:-4]
    
    def open_data(self) -> IO:
        pass
            
    def __repr__(self) -> str:
        return super().__repr__()