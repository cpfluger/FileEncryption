from random import randint
from Models import RSAKeyModel
from Cryptodome.Cipher import AES
from KeyGeneration import *

class Cryptography():

    def __init__(self, public_key, private_key):
        self._public_key = public_key
        self._private_key = private_key


    def get_public_key(self):
        return self._public_key


    def get_private_key(self):
        return self._private_key


    def encrypt(self, byte_array):
        pass


    def decrypt(self, byte_array):
        pass



class RSA(Cryptography):

    def __init__(self, public_key, private_key):
        super().__init__(public_key, private_key)


    def encrypt(self, clear_text_decimal_array):
        encrypted_text_decimal_array = []

        for element in clear_text_decimal_array:
            encrypted_text_decimal_array.append((element ** self._public_key.get_key_specific_number()) % self._public_key.get_prime_number_product())
            print(encrypted_text_decimal_array)
        return encrypted_text_decimal_array


    def decrypt(self, encrypted_text_decimal_array):
        clear_text_decimal_array = []

        for element in encrypted_text_decimal_array:
            clear_text_decimal_array.append((element ** self._private_key.get_key_specific_number()) % self._private_key.get_prime_number_product())
        return clear_text_decimal_array



class AES_Cipher(Cryptography):
  
    def __int__(self, public_key, private_key):
        super().__init__(public_key, private_key)

    def encrypt(self, byte_string):
        input = byte_string
        self.__tmp_array = []      
        self.__cipher = AES.new(self._public_key, AES.MODE_GCM)             
        ciphertext = self.__cipher.encrypt(input)
        self.__tmp_array.append(self.__cipher.nonce)
        self.__tmp_array.append(ciphertext)

        # sussy = b"".join([self.__tmp_array[0] , self.__tmp_array[1]])
        # print(len(self.__cipher.nonce)) 
        # print("ciphertext: " , self.__ciphertext)
        # print("nonce:" , self.__cipher.nonce)
        # output_len = len(self.__cipher.nonce)
        # print("ciphertext but as weird shit: " , sussy[output_len:])

        return b"".join([self.__tmp_array[0] , self.__tmp_array[1]])


    def decrypt(self, bytestring):
        self.bytestring = bytestring
        print(type(self.bytestring))
        self.__plaincipher = AES.new(self._public_key, AES.MODE_GCM,self.__tmp_array[0])
        self.__plaintext = self.__plaincipher.decrypt(self.__tmp_array[1])
        return self.__plaintext

