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



class AES(Cryptography):
  
    def __int__(self, public_key):
        super(AES, self).__init__(public_key, public_key)


    def encrypt(self, byte_array):
        self.__cipher = AES.new(self._public_key, AES.MODE_GCM)
        self.__ciphertext = self.__cipher.encrypt(byte_array)
        self.__file_out = open("encryptedfile.bin", "wb")
        [ self.__file_out.write(x) for x in (self.__cipher.nonce, self.__ciphertext) ]
        self.__file_out.close()


    def decrypt(self, byte_array):
        self.__file_in = open("encryptedfile.bin", "rb")
        self.__nonce, self.__ciphertext = [ self.__file_in.read(x) for x in (16, -1) ]
        self.__plaincipher = AES.new(self.__key, AES.MODE_GCM, self.__nonce)
        self.__plaintext = self.__plaincipher.decrypt(self.__ciphertext)

