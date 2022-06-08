import hashlib
from Cryptodome.Cipher import AES
from Cryptodome.Random import get_random_bytes
from Crypt_top_design import Cryptography, KeyGenerator


class AES_Cipher(Cryptography):
  
    def __int__(self, public_key, private_key):

        super(self).__init__(public_key, private_key)


    def encrypt(self, byte_string):

        input = byte_string
        cipher = AES.new(self._public_key, AES.MODE_GCM)
        ciphertext = cipher.encrypt(input)
        return b"".join([cipher.nonce , ciphertext])


    def decrypt(self, bytestring):

        bytestring = bytestring
        self.__plaincipher = AES.new(self._public_key, AES.MODE_GCM,bytestring[:16])
        plaintext = self.__plaincipher.decrypt(bytestring[16:])
        return plaintext



class AESKeyGeneration(KeyGenerator):
    
    def __int__(self):
        self.__password = None
        self.__salt = None
        self.__crypto_key = None


    def key_generate(self):
        self.__password = get_random_bytes(16)
        self.__salt = get_random_bytes(16)
        self.__crypto_key = hashlib.scrypt(password = self.__password, salt = self.__salt, n=2**14, r=8, p=1, dklen=16)


    def get_key(self):
        return self.__crypto_key
