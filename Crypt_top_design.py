

class Cryptography():

    def __init__(self, public_key, private_key):
        self._public_key = public_key
        self._private_key = private_key


    def get_public_key(self):
        return self._public_key


    def get_private_key(self):
        return self._private_key


class KeyGenerator():

    def __init__(self):
        pass

