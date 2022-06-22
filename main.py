import Conversion
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from Conversion import *
from AES import AES_Cipher, AESKeyGeneration
from RSA import *
import qdarktheme


if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = MainWindow()
    app.setStyleSheet(qdarktheme.load_stylesheet())
    w.show()
    sys.exit(app.exec_())











    
