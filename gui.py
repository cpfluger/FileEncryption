from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys


class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()
        self.filename = ""
        self.setAcceptDrops(True)

    def initUI(self):

        header = QLabel("Dateiverschlüsselung", self)
        header.move(20,10)
        
        font_header = QtGui.QFont()
        font_header.setPointSize(14)
        header.setFont(font_header)


        encrypt_btn = QPushButton("Encrypt", self)
        encrypt_btn.move(330,50)

        decrypt_btn = QPushButton("Decrypt", self)
        decrypt_btn.move(330,150)

        browse_btn = QPushButton("Browse...", self)
        browse_btn.move(30, 180)
        browse_btn.clicked.connect(self.browsefiles)

        self.text_input = QPlainTextEdit(self)
        self.text_input.setGeometry(30, 60, 260, 101)
        self.text_input.setPlaceholderText("Input your text here...")

        self.text_submit = QPushButton("Submit", self)
        self.text_submit.move(210, 170)
        self.text_submit.clicked.connect(self.submit)


        self.setWindowTitle("RSA-Encryption")
        self.setMinimumSize(520, 250)
        self.setMaximumSize(520, 250)
        self.show()


    def browsefiles(self):
        self.temp_path = QFileDialog.getOpenFileName(self, "Open File")
        print(self.temp_path[0])


    def submit(self):
        mytext = self.text_input.toPlainText()
        print(mytext)

    def AES_encrypt(self):
        pass

    def AES_decrpyt(self):
        pass

    def RSA_encrypt(self):
        pass

    def RSA_decrypt(self):
        pass

    def change_view_mode(self):
        pass

 
    

app = QApplication(sys.argv)
w = MainWindow()
sys.exit(app.exec_())
