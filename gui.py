from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.filename = ""

    def initUI(self):

        header = QLabel("Dateiverschlüsselung", self)
        header.move(20,10)
        
        font_header = QtGui.QFont()
        font_header.setPointSize(14)
        header.setFont(font_header)


        encrypt_btn = QPushButton("Encrypt Button", self)
        encrypt_btn.move(330,50)

        decrypt_btn = QPushButton("Decrypt Button", self)
        decrypt_btn.move(330,150)

        browse_btn = QPushButton("Browse...", self)
        browse_btn.move(30, 180)
        browse_btn.clicked.connect(self.browsefiles)

        self.setWindowTitle("RSA-Encryption")
        self.setMinimumSize(520, 250)
        self.setMaximumSize(520, 250)
        self.show()

    def browsefiles(self):
        self.temp_path = QFileDialog.getOpenFileName(self, "Open File")
        print(self.temp_path[0])



app = QApplication(sys.argv)
w = MainWindow()
sys.exit(app.exec_())
