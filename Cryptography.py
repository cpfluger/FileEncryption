from random import randint
from Models import RSAKeyModel
from Cryptodome.Cipher import AES

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


    def encrypt(self, byte_array):
        self.__input = byte_array
        self.__tmp_array = []           
        self.__cipher = AES.new(self._public_key, AES.MODE_GCM)             
        self.__ciphertext = self.__cipher.encrypt(self.__input)
        self.__tmp_array.append(self.__cipher.nonce)
        self.__tmp_array.append(self.__ciphertext)
        return self.__ciphertext


    def decrypt(self, byte_array):
        self.__input = byte_array
        self.__plaincipher = AES.new(self._public_key, AES.MODE_GCM, self.__tmp_array[0])
        self.__plaintext = self.__plaincipher.decrypt(self.__tmp_array[1])
        return self.__plaintext

