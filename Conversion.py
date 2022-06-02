def ascii_string_to_decimal(ascii_string):
    decimal_array = []

    for char in ascii_string:
        decimal_array.append(ord(char))
    return decimal_array


def decimal_array_to__ascii_string(decimal_array):
    ascii_string = []
    seperator = ""

    for char in decimal_array:
        ascii_string.append(chr(char))
    return seperator.join(ascii_string)


def string_to_bytestring(string_input):
    bytestring = bytes(string_input, 'utf_8')
    return bytestring


def bytestring_to_string(bystestring_input):
    string = bystestring_input.decode('latin-1')
    return string
