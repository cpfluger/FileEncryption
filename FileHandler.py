import os
class FileHandler():

    def __init__(self, file_name):
        self.__file_name = file_name
        self.__file_length = os.path.getsize(file_name)


    def get_file_name(self):
        return self.__file_name


    def read_all_bytes(self):
        file = open(self.__file_name, "r")
        read_bytes = file.read(self.__file_length)
        file.close()
        return read_bytes


    def overwrite_all_bytes(self, hex_string):
        file = open(self.__file_name, "w+")
        file.write(hex_string)
        file.close()

