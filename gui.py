from Conversion import *
from AES import AES_Cipher, AESKeyGeneration
from RSA import *
import qdarktheme
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import *
from FileHandler import *
import sys


class MainWindow(QMainWindow):

    def __init__(self):
        super().__init__()
        self.filename = ""
        self.RSA = None
        self.RSA_Key = None
        self.file_path = ""


    def initUI(self, FileEncryption):

        #----------Fonts------------
        headingfont = QtGui.QFont()
        headingfont.setPointSize(10)
        headingfont.setBold(True)
        headingfont.setWeight(75)

        basicfont = QtGui.QFont()
        basicfont.setPointSize(10)
        basicfont.setBold(False)
        basicfont.setWeight(50)

        FileEncryption.setObjectName("FileEncryption")
        FileEncryption.resize(1000, 700)
        FileEncryption.setMaximumSize(1000, 700)
        FileEncryption.setMinimumSize(1000, 700)
        FileEncryption.setWindowTitle("FileEncryption")
        FileEncryption.setWindowIcon(QtGui.QIcon('images/icon.png'))

        self.centralwidget = QWidget(FileEncryption)
        self.centralwidget.setObjectName("centralwidget")

        self.verticalLayoutWidget_2 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_2.setGeometry(QtCore.QRect(600, 650, 171, 101))


        self.header = QLabel(self.centralwidget)
        self.header.setGeometry(QtCore.QRect(40, 10, 311, 51))

        font = QtGui.QFont()
        font.setPointSize(15)
        font.setBold(True)
        font.setWeight(75)
        self.header.setFont(font)


        self.verticalLayoutWidget_3 = QWidget(self.centralwidget)
        self.verticalLayoutWidget_3.setGeometry(QtCore.QRect(520, 150, 251, 112))
 

        self.verticalLayout_3 = QVBoxLayout(self.verticalLayoutWidget_3)
        self.verticalLayout_3.setContentsMargins(0, 0, 0, 0)


        self.text_input_label = QLabel(self.verticalLayoutWidget_3)
        self.text_input_label.setFont(basicfont)
        self.verticalLayout_3.addWidget(self.text_input_label)

        self.text_input = QPlainTextEdit(self.verticalLayoutWidget_3)
        self.verticalLayout_3.addWidget(self.text_input)
        

        self.topline = QFrame(self.centralwidget)
        self.topline.setGeometry(QtCore.QRect(0, 60, 1011, 20))

        font = QtGui.QFont()
        font.setPointSize(18)
        self.topline.setFont(font)
        self.topline.setFrameShape(QFrame.HLine)
        self.topline.setFrameShadow(QFrame.Sunken)

        self.browse_btn = QPushButton(self.centralwidget)
        self.browse_btn.setGeometry(QtCore.QRect(90, 260, 93, 28))
        self.browse_btn.setFont(basicfont)
        self.browse_btn.clicked.connect(self.browsefiles_event)

        self.horizontalLayoutWidget = QWidget(self.centralwidget)
        self.horizontalLayoutWidget.setGeometry(QtCore.QRect(80, 80, 871, 51))
        self.horizontalLayoutWidget.setObjectName("horizontalLayoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.file_encrypt_option = QRadioButton(self.horizontalLayoutWidget)

        self.horizontalLayout.addWidget(self.file_encrypt_option)

        spacerItem = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem)

        self.text_encrypt_option = QRadioButton(self.horizontalLayoutWidget)
        
        self.horizontalLayout.addWidget(self.text_encrypt_option)
        spacerItem1 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout.addItem(spacerItem1)

        self.file_encrypt_option.setFont(headingfont)
        self.file_encrypt_option.setChecked(True)


        self.text_encrypt_option.setFont(headingfont)


        self.Drag_DropArea = QListWidget(self.centralwidget)
        self.Drag_DropArea.setGeometry(QtCore.QRect(90, 160, 256, 91))
        self.setAcceptDrops(True)
        self.setAutoFillBackground(True)

        self.centerlabel = QLabel(self.centralwidget)
        self.centerlabel.setGeometry(QtCore.QRect(190, 170, 131, 61))
        self.pixmap = QtGui.QPixmap('images/download2.png')
        self.centerlabel.setPixmap(self.pixmap)


        self.line_2 = QFrame(self.centralwidget)
        self.line_2.setGeometry(QtCore.QRect(450, 60, 21, 240))
        self.line_2.setFrameShape(QFrame.VLine)
        self.line_2.setFrameShadow(QFrame.Sunken)

        self.line_3 = QFrame(self.centralwidget)
        self.line_3.setGeometry(QtCore.QRect(-10, 300, 1341, 20))
        self.line_3.setFrameShape(QFrame.HLine)
        self.line_3.setFrameShadow(QFrame.Sunken)


        self.header_2 = QLabel(self.centralwidget)
        self.header_2.setGeometry(QtCore.QRect(730, 10, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.header_2.setFont(font)

        
        self.key_input = QTextEdit(self.centralwidget)
        self.key_input.setGeometry(QtCore.QRect(520, 400, 261, 40))
        self.key_input.setReadOnly(False)
        self.key_input.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)

        self.text_output = QTextEdit(self.centralwidget)
        self.text_output.setGeometry(QtCore.QRect(440, 570, 401, 81))
        self.text_output.setReadOnly(True)

        self.input_file_name = QLabel(self.centralwidget)
        self.input_file_name.setFont(basicfont)
        self.input_file_name.setGeometry(QtCore.QRect(210, 260, 250, 30))

        self.darkmode_btn = QPushButton(self.centralwidget)
        self.darkmode_btn.setGeometry(QtCore.QRect(580, 20, 121, 31))
        self.darkmode_btn.setFont(basicfont)
        self.darkmode_btn.clicked.connect(self.darkmode_event)
        self.darkmode_btn.setCheckable(True)

        self.encrypt_btn = QPushButton(self.centralwidget)
        self.encrypt_btn.setGeometry(QtCore.QRect(440, 520, 121, 41))
        self.encrypt_btn.setFont(headingfont)
        self.encrypt_btn.clicked.connect(self.encrypt_event)


        self.decrypt_btn = QPushButton(self.centralwidget)
        self.decrypt_btn.setGeometry(QtCore.QRect(720, 520, 121, 41))
        self.decrypt_btn.setFont(headingfont)
        self.decrypt_btn.clicked.connect(self.decrypt_event)

        self.horizontalLayoutWidget_2 = QtWidgets.QWidget(self.centralwidget)
        self.horizontalLayoutWidget_2.setGeometry(QtCore.QRect(80, 320, 871, 61))
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.horizontalLayoutWidget_2)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")

        spacerItem2 = QtWidgets.QSpacerItem(40, 20, QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Minimum)
        self.rsa_option = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.rsa_option.setFont(basicfont)
        self.rsa_option.setChecked(True)
        self.horizontalLayout_2.addWidget(self.rsa_option)
        self.horizontalLayout_2.addItem(spacerItem2)

        self.aes_option = QtWidgets.QRadioButton(self.horizontalLayoutWidget_2)
        self.aes_option.setFont(basicfont)
        self.horizontalLayout_2.addWidget(self.aes_option)
        spacerItem3 = QtWidgets.QSpacerItem(100, 50, QtWidgets.QSizePolicy.Fixed, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem3)
        

        self.generate_key_button = QtWidgets.QPushButton(self.horizontalLayoutWidget_2)
        self.generate_key_button.setFont(headingfont)
        self.generate_key_button.clicked.connect(self.generate_key)

        self.horizontalLayout_2.addWidget(self.generate_key_button)
        spacerItem4 = QtWidgets.QSpacerItem(70, 20, QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Minimum)
        self.horizontalLayout_2.addItem(spacerItem4)

        self.aes_label = QLabel(self.centralwidget)
        self.aes_label.setGeometry(QtCore.QRect(520, 380, 131, 16))
        self.aes_label.setFont(basicfont)

        self.public_key = QTextEdit(self.centralwidget)
        self.public_key.setGeometry(QtCore.QRect(80, 400, 261, 40))
        self.public_key.setReadOnly(False)
        self.public_key.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)

        self.private_key = QTextEdit(self.centralwidget)
        self.private_key.setGeometry(QtCore.QRect(80, 480, 261, 40))
        self.private_key.setReadOnly(False)
        self.private_key.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)

        self.prime_product = QTextEdit(self.centralwidget)
        self.prime_product.setGeometry(QtCore.QRect(80, 560, 261, 40))
        self.prime_product.setReadOnly(False)
        self.prime_product.setTextInteractionFlags(QtCore.Qt.TextEditorInteraction)

        self.error_box = QLabel(self.centralwidget)
        self.error_box.setFont(basicfont)
        self.error_box.setGeometry(QtCore.QRect(440, 480, 401, 21))

        FileEncryption.setCentralWidget(self.centralwidget)
        self.statusbar = QStatusBar(FileEncryption)
        FileEncryption.setStatusBar(self.statusbar)

        self.fillUi(FileEncryption)
        self.fillToolTipps()
        QtCore.QMetaObject.connectSlotsByName(FileEncryption)


    def fillUi(self, FileEncryption):

        _translate = QtCore.QCoreApplication.translate
        FileEncryption.setWindowTitle(_translate("FileEncryption", "FileEncryption"))
        self.header.setText(_translate("FileEncryption", "AES/RSA FileEncryption"))
        self.text_input_label.setText(_translate("FileEncryption", "Paste your text below:"))
        self.browse_btn.setText(_translate("FileEncryption", "Browse..."))
        self.file_encrypt_option.setText(_translate("FileEncryption", "File Encryption"))
        self.text_encrypt_option.setText(_translate("FileEncryption", "Text Encryption"))
        self.header_2.setText(_translate("FileEncryption", "by Lorenz, Elias & Clemens"))
        self.input_file_name.setText(_translate("FileEncryption", ""))
        self.darkmode_btn.setText(_translate("FileEncryption", "Darkmode"))
        self.encrypt_btn.setText(_translate("FileEncryption", "Encrypt"))
        self.decrypt_btn.setText(_translate("FileEncryption", "Decrypt"))
        self.rsa_option.setText(_translate("FileEncryption", "RSA - Encryption"))
        self.aes_option.setText(_translate("FileEncryption", "AES - Encryption"))
        self.generate_key_button.setText(_translate("FileEncryption", "Generate Key"))
        self.aes_label.setText(_translate("FileEncryption", "AES-Key:"))
        self.prime_product.setPlaceholderText("insert prime product")
        self.private_key.setPlaceholderText("insert private key")
        self.public_key.setPlaceholderText("insert public key")
        self.text_output.setPlaceholderText("Your decrypted text will spawn here...")
        self.key_input.setPlaceholderText("Generated Key")
        self.text_input.setPlaceholderText("Input your text here...")


    def fillToolTipps(self):

        self.rsa_option.setToolTip("Choose RSA encryption")
        self.decrypt_btn.setToolTip("Press Button to decrypt")
        self.encrypt_btn.setToolTip("Press Button to encrypt")
        self.aes_option.setToolTip("Choose AES encryption")
        self.darkmode_btn.setToolTip("Set Design to Darkmode")
        self.text_input.setToolTip("Copy your key here")
        self.browse_btn.setToolTip("Open File Explorer")


    #---------------------------------------------EVENTS-------------------------------------------------#

    def encrypt_event(self):

        self.text_output.setPlainText("")
        if self.rsa_option.isChecked():
            self.RSA_encrypt()

        elif self.aes_option.isChecked():
            self.AES_encrypt()


    def decrypt_event(self):

        self.text_output.setPlainText("")
        if self.rsa_option.isChecked():
            self.RSA_decrypt()
        elif self.aes_option.isChecked():
            self.AES_decrypt()


    def darkmode_event(self):

        if self.darkmode_btn.isChecked():
            app.setStyleSheet(qdarktheme.load_stylesheet("light"))
            self.pixmap = QtGui.QPixmap('images/download1.png')
            self.centerlabel.setPixmap(self.pixmap)

        else:
            app.setStyleSheet(qdarktheme.load_stylesheet())
            self.pixmap = QtGui.QPixmap('images/download2.png')
            self.centerlabel.setPixmap(self.pixmap)


    def generate_key(self):

        if self.rsa_option.isChecked():
            self.generate_rsa_key()

        elif self.aes_option.isChecked():
            self.generate_aes_key()


    def error_message(self, input):

        self.error_box.setText("")
        self.error_box.setText(input)


    def dragEnterEvent(self, event):

        if event.mimeData().hasUrls:
            event.accept()
        else:
            event.ignore()


    def dropEvent(self, event):

        files = [u.toLocalFile() for u in event.mimeData().urls()]
        for f in files:
            print(f)


    def browsefiles_event(self):

        self.temp_path = QFileDialog.getOpenFileName(self, "Open File")
        self.file_path = self.temp_path[0]
        self.update_file()
        self.input_file_name.setText(self.file_path)


    def update_file(self):

        self.file_input = FileHandler(self.file_path)
        self.file_input_content = self.file_input.read_all_bytes()


    def submit_encrypt(self):

        self.mytext = self.text_input.toPlainText()


    #----------------------------------------Encrypt & Decrypt--------------------------------------------#

    def AES_encrypt(self):
        
        if self.check_if_input_is_empty() == False:
            
            if self.check_if_input_is_hex() == False:

                if self.check_if_aes_key_is_empty() == False:

                    if self.check_if_aes_key_is_hex() == True:
                        
                        if self.file_encrypt_option.isChecked() == True:
                            
                            self.update_file()
                            inputtext = self.file_input_content
                            encrypted_input = self.AES_Cipher.encrypt(string_to_bytestring(inputtext))               #encrypt the converted input text
                            self.file_input.overwrite_all_bytes(byte_string_to_hex_string(encrypted_input))
                            self.text_output.setPlainText(byte_string_to_hex_string(encrypted_input))
                        else:
                            inputtext = self.text_input.toPlainText()                                                #get input from input field
                            encrypted_input = self.AES_Cipher.encrypt(string_to_bytestring(inputtext))               #encrypt the converted input text
                            self.text_output.setPlainText(byte_string_to_hex_string(encrypted_input))                #stringing the bytestring to make it possible to put it inot the qplaintextedit
                else:
                    self.error_message("Please Input a Key first.")
            else:
                self.error_message("Please Input a non encryptet Text")  
        else:
            self.error_message("Please Input a Text / File")


    def AES_decrypt(self):
        
        if self.check_if_input_is_empty() == False:

            if self.check_if_input_is_hex() == True:
    
                if self.check_if_aes_key_is_empty() == False:

                    if self.check_if_aes_key_is_hex() == True:
                    
                        if self.file_encrypt_option.isChecked() == True:
                            encrypted_txt = self.file_input_content
                            mytext = self.AES_Cipher.decrypt(hex_string_to_byte_string(encrypted_txt))
                            self.file_input.overwrite_all_bytes(bytestring_to_string(mytext))
                            self.text_output.setPlainText(bytestring_to_string(mytext))                            

                        else:

                            encrypted_txt = self.text_input.toPlainText()                                      #write output to field  output = string b'\xFF'
                            mytext = self.AES_Cipher.decrypt(hex_string_to_byte_string(encrypted_txt))
                            self.text_output.setPlainText(bytestring_to_string(mytext))
                else:
                    self.error_message("Please Input a Key first.")            
            else:
                self.error_message("Please input an encrypted text")

        else:
            self.error_message("Please Input a Text")


    def RSA_encrypt(self):
        if self.check_if_input_is_empty() == False:

            if self.check_if_input_is_hex() == False:

                if self.check_if_rsa_key_is_empty() == False:

                    if self.check_if_rsa_key_is_hex() == True:

                        if self.file_encrypt_option.isChecked() == True:
                            self.update_file()
                            inputtext = self.file_input_content
                            encrypted_input = self.RSA.encrypt(ascii_string_to_decimal(inputtext))  # encrypt the converted input text
                            self.file_input.overwrite_all_bytes(decimal_array_to_hex_string(encrypted_input))
                            self.text_output.setPlainText(decimal_array_to_hex_string(encrypted_input))

                        else:
                            inputtext = self.text_input.toPlainText()  # get input from input field
                            encrypted_input = self.RSA.encrypt(ascii_string_to_decimal(inputtext))  # encrypt the converted input text
                            self.text_output.setPlainText(decimal_array_to_hex_string(encrypted_input))  # stringing the bytestring to make it possible to put it inot the qplaintextedit
                else:
                    self.error_message("Please Input a Key Pair first.")
            else:
                self.error_message("Please Input a non encryptet Text")
        else:
            self.error_message("Please Input a Text / File")


    def RSA_decrypt(self):

        if self.check_if_input_is_empty() == False:

            if self.check_if_input_is_hex() == True:

                if self.check_if_rsa_key_is_empty() == False:

                    if self.check_if_rsa_key_is_hex() == True:

                        if self.file_encrypt_option.isChecked() == True:
                            encrypted_txt = self.file_input_content
                            mytext = self.RSA.decrypt(hex_string_to_decimal_array(encrypted_txt))
                            self.file_input.overwrite_all_bytes(decimal_array_to__ascii_string(mytext))
                            self.text_output.setPlainText(decimal_array_to__ascii_string(mytext))

                        else:

                            encrypted_txt = self.text_input.toPlainText()  # write output to field  output = string b'\xFF'
                            mytext = self.RSA.decrypt(hex_string_to_decimal_array(encrypted_txt))
                            self.text_output.setPlainText(decimal_array_to__ascii_string(mytext))
                else:
                    self.error_message("Please Input a Key Pair first.")
            else:
                self.error_message("Please input an encrypted text")

        else:
            self.error_message("Please Input a Text")

    #---------------------------------------Key Operations------------------------------------------------#

    def check_if_aes_key_is_empty(self):

        if self.key_input.toPlainText() == "":
            self.error_message("Pls generate a Key first, or insert a valid one yourself!")
            return True

        else:
            if self.check_if_aes_key_is_hex() == False:
                self.error_message("Please input a hex key")
                return False
            
            elif self.check_if_aes_key_is_hex() == True:
                self.error_message("Working with the given Key")
                aes_working_key = hex_string_to_byte_string(self.key_input.toPlainText())
                self.AES_Cipher = AES_Cipher(aes_working_key, aes_working_key)
                return False


    def check_if_rsa_key_is_empty(self):

        if self.public_key.toPlainText() == "" and self.prime_product.toPlainText() == "" and self.private_key.toPlainText() == "":
            self.error_message("Pls generate a Key Pair first, or insert a valide one yourself!")
            return True

        else:
            if self.check_if_rsa_key_is_hex() == False:
                self.error_message("Please input a hex key")
                return False

            elif self.check_if_rsa_key_is_hex() == True:
                self.error_message("Working with the given Key")
                rsa_working_key = [int(self.public_key.toPlainText().replace("0x", ""), 16), int(self.private_key.toPlainText().replace("0x", ""), 16), int(self.prime_product.toPlainText().replace("0x", ""), 16)]
                self.RSA = RSA(RSAKeyModel(rsa_working_key[2], rsa_working_key[0]), RSAKeyModel(rsa_working_key[2], rsa_working_key[1]))
                return False


    def generate_aes_key(self):

        if self.check_if_input_is_empty() == False:

            if self.check_if_input_is_hex() == True:
                self.error_message("You can't generate a Key when you want to decrypt")

            else:
                self.aes_key = AESKeyGeneration()
                self.aes_key.key_generate()
                self.AES_Cipher = AES_Cipher(self.aes_key.get_key(), self.aes_key.get_key())
                self.key_input.setPlainText(byte_string_to_hex_string(self.aes_key.get_key()))
                self.error_message("Key successfully generated")

        else:
            self.error_message("Please input a Text or File first")


    def generate_rsa_key(self):

        if self.check_if_input_is_empty() == False:

            if self.check_if_input_is_hex() == True:

                self.error_message("You can't generate a Key when you want to decrypt")

            else:
                self.RSA_Key = RSAKeyGenerator()
                self.RSA_Key.load_generator(265)
                self.RSA = RSA(self.RSA_Key.get_public_key(), self.RSA_Key.get_private_key())

                self.public_key.setPlainText(hex(self.RSA_Key.get_public_key().get_key_specific_number()))
                self.private_key.setPlainText(hex(self.RSA_Key.get_private_key().get_key_specific_number()))
                self.prime_product.setPlainText(hex(self.RSA_Key.get_private_key().get_prime_number_product()))
                self.error_message("RSA-Key successfully generated")
        else:
            self.error_message("Please input a Text or File first")


    #--------------------------------------input checks---------------------------------------------------#

    def check_if_input_is_hex(self):

        if self.file_encrypt_option.isChecked():
            self.update_file()
            input = self.file_input_content
            if input[0:2] == "0x":
                return True
            else:
                return False
        else:
            input = self.text_input.toPlainText()
            if input[0:2] == "0x":
                return True
            else:
                return False


    def check_if_input_is_empty(self):

        if self.file_encrypt_option.isChecked() == True:
            if self.file_path == "":
                return True
            else:
                return False

        elif self.text_encrypt_option.isChecked() == True:
            if self.text_input.toPlainText() == "":
                return True
            else:
                return False


    def check_if_aes_key_is_hex(self):

        input = self.key_input.toPlainText()
        if input[0:2] == "0x":
            return True
        else:
            return False


    def check_if_rsa_key_is_hex(self):

        input = [self.public_key.toPlainText(), self.private_key.toPlainText(), self.prime_product.toPlainText()]
        return_flag = True

        for text in input:
            if text[0:2] != "0x":
                return_flag = False
        return return_flag


#------------------------------------------main program---------------------------------------------------#      

if __name__ == "__main__":

    app = QApplication(sys.argv)
    app.setStyleSheet(qdarktheme.load_stylesheet())
    FileEncryption = QMainWindow()
    ui = MainWindow()
    ui.initUI(FileEncryption)
    FileEncryption.show()
    sys.exit(app.exec_())
