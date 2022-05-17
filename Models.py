class RSAKeyModel():

    def __init__(self, prime_number_product, key_specific_number):
        self.__prime_number_product = prime_number_product
        self.__key_specific_number = key_specific_number


    def get_prime_number_product(self):
        return self.__prime_number_product


    def get_key_specific_number(self):
        return self.__key_specific_number
