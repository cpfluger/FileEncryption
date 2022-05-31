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
