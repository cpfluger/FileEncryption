from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys
from Cryptography import AES_Cipher


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
        encrypt_btn.move(330,120)
        encrypt_btn.clicked.connect(self.encrypt_event)

        decrypt_btn = QPushButton("Decrypt", self)
        decrypt_btn.move(330,150)
        decrypt_btn.clicked.connect(self.decrypt_event)

        browse_btn = QPushButton("Browse...", self)
        browse_btn.move(30, 190)
        browse_btn.clicked.connect(self.browsefiles)

        self.text_input = QPlainTextEdit(self)
        self.text_input.setGeometry(20, 80, 260, 101)
        self.text_input.setPlaceholderText("Input your text here...")

        self.text_submit = QPushButton("Submit", self)
        self.text_submit.move(200, 190)
        self.text_submit.clicked.connect(self.submit)

        self.rsa_option = QRadioButton("RSA", self)
        self.rsa_option.move(330, 50)
        self.rsa_option.setChecked(True)

        self.aes_option = QRadioButton("AES", self)
        self.aes_option.move(330, 70)


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

    #------------EVENTS-----------------------------------------------------#

    def encrypt_event(self):
        if self.rsa_option.isChecked():
            pass
        else:
            pass


    def decrypt_event(self):
        if self.rsa_option.isChecked():
            pass
        else:
            pass



    

    # def encrypt(self):
    #     if self.rsa_option.isChecked():
            
    #     else:
                
    # def decrypt(self):
    #     pass

    # def RSA_encrypt(self):
    #     pass

    # def RSA_decrypt(self):
    #     pass

 
    

app = QApplication(sys.argv)
w = MainWindow()
sys.exit(app.exec_())
