from components import conversions

# A predefined salter list
salter = [11, 32, 17, 25, 9, 25, 2, 20, 5, 13, 18, 6, 22, 14, 33, 35]


def salt(password):
    global salter

    # Ensure password is at least 16 characters
    while len(password) < 16:
        password += password

    # Limit password to 16 characters
    new_password = password[:16]

    # Shift each character in the new_password
    converted_list = ''
    for i in range(len(new_password)):
        c = ord(new_password[i]) + salter[i]
        if c > 126:
            c = c % 127 + 33
        converted_list += chr(c)

    return converted_list


def create_bitstream(password, encodings):
    # Convert password to bitstream using encodings
    bitstream = ''
    for char in password:
        bitstream += encodings[char]
    return bitstream


def hexify(bitstream):
    # Convert bitstream to hex
    hex_result = ''
    bin2hex = conversions.bin2hex
    for i in range(0, len(bitstream), 4):
        bit = bitstream[i:i + 4]
        hex_value = bin2hex.get(bit)
        hex_result += hex_value
    return hex_result


def asciify(hexstring):
    # Convert hex string to ASCII characters
    astream = ''
    for i in range(0, len(hexstring), 2):
        d1 = conversions.hex2deci.get(hexstring[i])
        d2 = conversions.hex2deci.get(hexstring[i + 1])
        d = d1 * 8 + d2 + 33
        if d > 126:
            d = d % 127 + 33
        astream += chr(d)
    return astream


def encrypt(password):
    # Encrypt password
    salted = salt(password)
    bitstreamed = create_bitstream(salted, conversions.encodings)
    hexed = hexify(bitstreamed)
    asciied = asciify(hexed)
    return asciied


if __name__ == '__main__':
    password = 'sMiLe:-)'
    encrypted = encrypt(password)
    print(encrypted)
