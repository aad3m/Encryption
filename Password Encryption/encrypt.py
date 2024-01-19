import conversions
import database

# test salter that was randomly generated
salter = [11, 32, 17, 25, 9, 25, 2, 20, 5, 13, 18, 6, 22, 14, 33, 35]
def salt(password):

    # use the salter defined in the global scope of this file
    global salter
    # makes password 16 characters
    while len(password) < 16:
        password += password
    # limits new password t 16
    new_password = password[:16]

    # iterates over new_password to convert to shifted character
    converted_list = ''
    for i in range(len(new_password)):
        c = ord(new_password[i]) + salter[i]
        if c > 126:
            c = c % 127 + 33
        converted_list += chr(c)



    return converted_list

def create_bitstream(password,encodings):

    # define bitsream
    bitstream = ''

    # each character in password
    for char in password:
        # adds ecnoding to bitstream
        bitstream += encodings[char]

    return bitstream

def hexify(bitstream):

    # define hex_result
    hex_result = ''

    # use bin2hex from convnersions
    bin2hex = conversions.bin2hex
    # 4 characters lenght
    for i in range(0,len(bitstream), 4):
        # define one bit as 4 characters
        bit = bitstream[i:i + 4]
        # change bit to hex
        hex_value = bin2hex.get(bit)
        # add new value to result
        hex_result += hex_value

    return hex_result




def asciify(hexstring):

    # define astream
    astream = ''

    # 2 characters lenght
    for i in range(0,len(hexstring), 2):
        # get deci value for hex
        d1 = conversions.hex2deci.get(hexstring[i])
        d2 = conversions.hex2deci.get(hexstring[i+1])
        d = d1*8 + d2 + 33
        if d > 126:
            d = d % 127 + 33
        astream += chr(d)
    return astream

def encrypt(password):
    # salt
    salted = salt(password)
    # bitstream
    bitstreamed = create_bitstream(salted, conversions.encodings)
    # hexify
    hexed = hexify(bitstreamed)
    # asciify
    asciied = asciify(hexed)


    return asciied



if __name__ == '__main__':
    password = 'sMiLe:-)'
    encrypted = encrypt(password)
    print(encrypted)


