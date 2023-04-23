from ui_design import Ui_MainWindow
import sys
from PyQt5.QtWidgets import QMainWindow, QApplication
from threading import *
from metots import Loop
from PyQt5.QtWidgets import QFileDialog
import os

class MainWindow:
    def __init__(self):
        self.main_win = QMainWindow()
        self.main_win.showMaximized()
        self.loop = Loop()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self.main_win)
        self.open_file_path = None
        self.save_file_path = None

        self.ui.pushButton_Open.clicked.connect(self.open_file_name)
        self.ui.pushButton_Save_File.clicked.connect(self.save_file_name)
        self.ui.pushButton_Run.clicked.connect(self.run_thread)
        # self.ui.pushButton_Preview.clicked.connect(self.loop.preview)

    def run_thread(self):
        """
        It creates a thread and starts it.
        """
        t1 = Thread(target=self.run)
        t1.start()

    def run(self):
        self.loop.loop(
            open_file=self.open_file_path,
            save_file= self.save_file_path,
            number_of_copy=self.ui.spinBox_number.text(),
            shift_x=self.ui.lineEdit_x_shift.text(),
            shift_y=self.ui.lineEdit_y_shift.text(),
            random_noise=self.ui.checkBox_Noise.isChecked(),
            random_contrast=self.ui.checkBox_Contrast.isChecked(),
            random_sharpness=self.ui.checkBox_Sharpness.isChecked(),
            random_brightness=self.ui.checkBox_Brigness.isChecked())
        
    def open_file_name(self):
            self.open_file_path = QFileDialog.getExistingDirectory(caption='Choose Directory',
                                                         directory=os.path.expanduser("~/Desktop"))
        
    def save_file_name(self):
            self.save_file_path = QFileDialog.getExistingDirectory(caption='Choose Directory',
                                                         directory=os.path.expanduser("~/Desktop"))    
            
    def show(self):
        """
        The function `show()` is a method of the class `MainWindow` and it is called on the object `self`
        (which is the object of the class `MainWindow`)
        """
        self.main_win.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_win = MainWindow()
    main_win.show()
    sys.exit(app.exec())
