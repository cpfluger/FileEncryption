import qdarktheme
from PyQt5.QtWidgets import *
import sys
from gui import MainWindow

if __name__ == '__main__':

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarktheme.load_stylesheet())
    w = MainWindow()
    sys.exit(app.exec_())











    
