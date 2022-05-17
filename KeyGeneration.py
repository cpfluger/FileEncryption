from CalculationAuxiliary import get_low_level_prime, \
    is_miller_rabin_passed, is_relatively_prime_to, extended_euclidic_algortihtm
from Models import RSAKeyModel


class KeyGenerator():

    def __init__(self):
        pass



class RSAKeyGenerator(KeyGenerator):

    def __int__(self):
        self.__prime_number_p = None
        self.__prime_number_q = None
        self.__product_number_n = None
        self.__eulers_totient_z = None
        self.__encryption_number_e = None
        self.__decryption_number_d = None


    def load_generator(self, key_length_bit):
        self.__prime_number_p = self.create_prime_number(key_length_bit)
        self.__prime_number_q = self.create_prime_number(key_length_bit)
        self.__product_number_n = self.__prime_number_p * self.__prime_number_q
        self.__eulers_totient_z = (self.__prime_number_p - 1) * (self.__prime_number_q - 1)
        self.generate_encryption_number()
        self.generate_decryption_number()


    def get_public_key(self):
        return RSAKeyModel(self.__product_number_n, self.__encryption_number_e)


    def get_private_key(self):
        return RSAKeyModel(self.__product_number_n, self.__decryption_number_d)


    def generate_encryption_number(self):
        potential_encryption_number = self.__eulers_totient_z - 1000

        while not is_relatively_prime_to(self.__eulers_totient_z, potential_encryption_number):
            potential_encryption_number = potential_encryption_number - 1
        self.__encryption_number_e = int(potential_encryption_number)


    def generate_decryption_number(self):
        g, u, v = extended_euclidic_algortihtm(self.__encryption_number_e, self.__product_number_n)
        self.__decryption_number_d = u % self.__product_number_n


    def create_prime_number(self, number_of_bits):
        while True:
            prime_candidate = get_low_level_prime(number_of_bits)
            if is_miller_rabin_passed(prime_candidate):
                return prime_candidate



class AESKeyGenerator(KeyGenerator):
    def __int__(self):
        print("clemi sus")

    def generate_private_key(self):
        pass


    def generate_public_key(self):
        pass