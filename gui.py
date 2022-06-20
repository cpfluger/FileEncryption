import Conversion
from PyQt5.QtWidgets import *
from PyQt5 import QtGui
from Conversion import *
from AES import AES_Cipher, AESKeyGeneration
from RSA import *
import qdarktheme


class MainWindow(QWidget):


    def __init__(self):
        super().__init__()
        self.initUI()
        self.filename = ""
        self.setAcceptDrops(True)
        self.RSA = None
        self.RSA_Key = None



    def initUI(self):

        header = QLabel("FileEncryption", self)
        header.move(20,10)
        
        font_header = QtGui.QFont()
        font_header.setPointSize(14)
        header.setFont(font_header)

        self.darkmode_btn = QPushButton("Darkmode", self)
        self.darkmode_btn.move(400, 10)
        self.darkmode_btn.setCheckable(True)
        self.darkmode_btn.clicked.connect(self.darkmode_event)
        self.darkmode_btn.setToolTip("Set Design to Darkmode")


        encrypt_btn = QPushButton("Encrypt", self)
        encrypt_btn.move(330,100)
        # encrypt_btn.clicked.connect(self.submit_encrypt)
        encrypt_btn.clicked.connect(self.encrypt_event)
        encrypt_btn.setToolTip("Press Button to encrypt")

        decrypt_btn = QPushButton("Decrypt", self)
        decrypt_btn.move(330,130)
        decrypt_btn.clicked.connect(self.decrypt_event)
        decrypt_btn.setToolTip("Press Button to decrypt")

        browse_btn = QPushButton("Browse...", self)
        browse_btn.move(30, 190)
        browse_btn.clicked.connect(self.browsefiles)
        browse_btn.setToolTip("Open File Explorer")

        self.text_input = QPlainTextEdit(self)
        self.text_input.setGeometry(20, 80, 260, 40)
        self.text_input.setPlaceholderText("Input your text here...")
        

        self.text_output = QPlainTextEdit(self)
        self.text_output.setGeometry(20, 130, 260, 40)
        self.text_output.setPlaceholderText("Your decrypted text will spawn here...")

        self.rsa_option = QRadioButton("RSA", self)
        self.rsa_option.move(330, 50)
        self.rsa_option.setChecked(True)
        self.rsa_option.setToolTip("Choose RSA encryption")

        self.aes_option = QRadioButton("AES", self)
        self.aes_option.move(330, 70)
        self.aes_option.setToolTip("Choose AES encryption")

        self.key_input = QTextEdit(self)
        self.key_input.setGeometry(330, 160, 180, 30)
        self.key_input.setPlaceholderText("Input your key")
        self.text_input.setToolTip("Copy your key here")

        self.key_output = QTextEdit(self)
        self.key_output.setGeometry(330, 200, 180, 30)
        self.key_output.setPlaceholderText("Your Key")


        self.setWindowTitle("FileEncryption")
        self.setWindowIcon(QtGui.QIcon('images/icon.png'))
        self.setMinimumSize(520, 250)
        self.setMaximumSize(520, 250)
        self.show()


    def browsefiles(self):
        self.temp_path = QFileDialog.getOpenFileName(self, "Open File")
        print(self.temp_path[0])


    def submit_encrypt(self):
        self.mytext = self.text_input.toPlainText()


    #---------------------------------EVENTS-------------------------------------------#

    def encrypt_event(self):
        if self.rsa_option.isChecked():
            self.check_key_rsa()
            self.RSA_encrypt()
        elif self.aes_option.isChecked():
            self.AES_encrypt()

    def decrypt_event(self):
        if self.rsa_option.isChecked():
            self.RSA_decrypt()
        elif self.aes_option.isChecked():
            self.AES_decrypt()
    
    def darkmode_event(self):
        if self.darkmode_btn.isChecked():
            app.setStyleSheet('Windows')
        else:
            app.setStyleSheet(qdarktheme.load_stylesheet())

    #--------------------------------Encrypt & Decrypt---------------------------------#  
      
    def AES_encrypt(self):
        self.check_key_status()
        self.key_input.setPlainText(bytestring_to_string(self.aes_key))

        inputtext = self.text_input.toPlainText()                                           #get input from input field
        encrypted_input = self.AES_Cipher.encrypt(string_to_bytestring(inputtext))          #encrypt the converted input text
        self.text_output.setPlainText(bytestring_to_string(encrypted_input))                #stringing the bytestring to make it possible to put it inot the qplaintextedit


    def AES_decrypt(self):
        encrypted_txt = self.text_output.toPlainText()                                      #write output to field  output = string b'\xFF'
        mytext = self.AES_Cipher.decrypt(string_to_bytestring(encrypted_txt))
        self.text_input.setPlainText(bytestring_to_string(mytext))


    def RSA_encrypt(self):
        inputtext = self.text_input.toPlainText()
        encrypted_input = self.RSA.encrypt(ascii_string_to_decimal(inputtext))
        self.text_output.setPlainText(decimal_array_to_hex_string(encrypted_input))


    def RSA_decrypt(self):
        encrypted_text = self.text_output.toPlainText()
        decrypted_text = self.RSA.decrypt(hex_string_to_decimal_array(encrypted_text))
        self.text_input.setPlainText(decimal_array_to__ascii_string(decrypted_text))

 
    #-----------------------------------------Key Operations-------------------------------------------#


    def check_key_status(self):

        if self.key_input.toPlainText() == "":
            print("generating Key")
            self.aes_key = AESKeyGeneration()
            self.aes_key.key_generate()
            self.AES_Cipher = AES_Cipher(self.aes_key.get_key(), self.aes_key.get_key())

        else:
            print("taking your key")
            self.aes_key = string_to_bytestring(self.key_input.toPlainText())
            self.AES_Cipher = AES_Cipher(self.aes_key, self.aes_key)


    def check_key_rsa(self):
        if self.key_input.toPlainText() == "":
            print("generating Key")
            self.RSA_Key = RSAKeyGenerator()
            self.RSA_Key.load_generator(265)
            self.RSA = RSA(self.RSA_Key.get_public_key(), self.RSA_Key.get_private_key())

        elif "0x" in self.key_input.toPlainText() and "0x" in self.key_input.toPlainText():
            print("taking your key")
            self.RSA = RSA(123, 123) #temporary


