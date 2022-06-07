from PyQt5.QtWidgets import *
from PyQt5 import QtGui
import sys
from Cryptography import AES_Cipher
from KeyGeneration import *
from Conversion import *


class MainWindow(QWidget):


    def __init__(self):
        super().__init__()
        self.initUI()
        self.filename = ""
        self.setAcceptDrops(True)

        #AES-Stuff
        self.AES_Key = AESKeyGeneration()
        self.AES_Key.key_generate()
        self.AES_Cipher = AES_Cipher(self.AES_Key.get_key(), self.AES_Key.get_key())


    def initUI(self):

        header = QLabel("Dateiverschlüsselung", self)
        header.move(20,10)
        
        font_header = QtGui.QFont()
        font_header.setPointSize(14)
        header.setFont(font_header)


        encrypt_btn = QPushButton("Encrypt", self)
        encrypt_btn.move(330,120)
        # encrypt_btn.clicked.connect(self.submit_encrypt)
        encrypt_btn.clicked.connect(self.encrypt_event)

        decrypt_btn = QPushButton("Decrypt", self)
        decrypt_btn.move(330,150)
        decrypt_btn.clicked.connect(self.decrypt_event)

        browse_btn = QPushButton("Browse...", self)
        browse_btn.move(30, 190)
        browse_btn.clicked.connect(self.browsefiles)

        self.text_input = QPlainTextEdit(self)
        self.text_input.setGeometry(20, 80, 260, 40)
        self.text_input.setPlaceholderText("Input your text here...")

        self.text_output = QPlainTextEdit(self)
        self.text_output.setGeometry(20, 130, 260, 40)
        self.text_output.setPlaceholderText("Your decrypted text will spawn here...")

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


    # def submit_encrypt(self):
    #     self.mytext = self.text_input.toPlainText()


    #---------------------------------EVENTS-------------------------------------------#

    def encrypt_event(self):
        if self.rsa_option.isChecked():
            self.RSA_encrypt()
        elif self.aes_option.isChecked():
            self.AES_encrypt()

    def decrypt_event(self):
        if self.rsa_option.isChecked():
            self.RSA_decrypt()
        elif self.aes_option.isChecked():
            self.AES_decrypt()

    #--------------------------------Encrypt & Decrypt---------------------------------#  
      
    def AES_encrypt(self):

        inputtext = self.text_input.toPlainText()                                           #get input from input field
        encrypted_input = self.AES_Cipher.encrypt(string_to_bytestring(inputtext))          #encrypt the converted input text
        self.text_output.setPlainText(bytestring_to_string(encrypted_input))                #stringing the bytestring to make it possible to put it inot the qplaintextedit


    def AES_decrypt(self):

        encrypted_txt = self.text_output.toPlainText()                                      #write output to field  output = string b'\xFF'
        mytext = self.AES_Cipher.decrypt(string_to_bytestring(encrypted_txt))
        self.text_input.setPlainText(bytestring_to_string(mytext)) 



    def RSA_encrypt(self):
        print("RSA_encrypt")


    def RSA_decrypt(self):
        print("RSA_decrypt")

 
    

app = QApplication(sys.argv)
w = MainWindow()
sys.exit(app.exec_())
