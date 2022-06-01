from CalculationAuxiliary import get_low_level_prime, is_miller_rabin_passed, \
    is_relatively_prime_to, euclidic_algorithm
from KeyGeneration import RSAKeyGenerator, AESKeyGeneration, KeyGenerator
from Cryptography import RSA, AES_Cipher, Cryptography
from Models import RSAKeyModel


if __name__ == '__main__':
    
    #generating private and public RSA keys
    obj = RSAKeyGenerator()
    obj.load_generator(8)   #8bit prime numbers for key generation work pretty well, 128bit throws a "memory error" exception after long time calculating, please execute on pc with high ram ressources
    pubkey = obj.get_public_key()
    privkey = obj.get_private_key()

    n = pubkey.get_prime_number_product()
    e = pubkey.get_key_specific_number()
    d = privkey.get_key_specific_number()
    nd = privkey.get_prime_number_product()

    print("n: {}".format(n))
    print("e: {}".format(e))
    print("n(priv): {}".format(nd))
    print("d: {}".format(d))
    
    #en - decrypting list of ints
    rsa = RSA(pubkey, privkey)
    encr = rsa.encrypt([1, 2, 3, 6])
    print(encr)
    decr = rsa.decrypt(encr)
    print(decr)

    # def aes_encrypt(input):
    #     key = AESKeyGeneration()
    #     key.key_generate()
    #     crypto_key = key.get_key()



    # #AES key generation
    key = AESKeyGeneration()
    key.key_generate()
    crypto_key = key.get_key()

    aes = AES_Cipher(crypto_key, crypto_key)
    aes_encr = aes.encrypt(b'ich bin ein plaintext')
    print(aes_encr)
    aes_decr = aes.decrypt(aes_encr)
    print(aes_decr)













    
