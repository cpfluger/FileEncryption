def ascii_string_to_decimal(ascii_string):
    decimal_array = []

    for char in ascii_string:
        decimal_array.append(ord(char))
    return decimal_array


def decimal_array_to__ascii_string(decimal_array):
    ascii_string = []
    seperator = ""

    for dec in decimal_array:
        ascii_string.append(chr(dec))
    return seperator.join(ascii_string)


def decimal_array_to_hex_array(decimal_array):
    hex_array = []

    for dec in decimal_array:
        hex_array.append(hex(dec))
    return hex_array


def hex_array_to_decimal_array(hex_array):
    decimal_array = []

    for hex in hex_array:
        decimal_array.append(int(hex))
    return decimal_array


def decimal_array_to_hex_string(decimal_array):
    hex_list = [hex(c) for c in decimal_array]
    return "".join(hex_list)


def hex_string_to_decimal_array(hex_string):
    hex_array = hex_string.split("0x")
    hex_array.pop(0)
    for c in hex_array:
        c = hex(int(c, 16))
    return hex_array


def string_to_bytestring(string_input):
    bytestring = bytes(string_input, 'latin-1')
    return str(bytestring)


def bytestring_to_string(bystestring_input):
    string = bystestring_input.decode('latin-1')
    return string
