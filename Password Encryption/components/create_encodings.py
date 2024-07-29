import random

# establish which range of characters using
starting_character = chr(33)
ending_character = chr(126)
character_count = ord(ending_character) - ord(starting_character) + 1

# arbitrary starting bit stream
starting_value = 0b1010100001

# length of each bitstream in the dictionary
bits_count = 10


def make_bitstreams():
    # randomly assign bitstreams to characters
    global starting_value

    # create empty list in which to place bitstreams
    list_bitstreams = [0] * character_count

    # create a list of indices 
    positions_remaining = [i for i in range(character_count)]
    current_value = starting_value
    # i corresponds to the remaining positions in the list
    for i in range(character_count - 1, -1, -1):
        # get the next bitstream and update the current value
        bitstream = add_one(current_value)
        current_value += 1

        # choose a random index into the positions_remaining
        next = random.randint(0, i)

        # place the next bitstream at that random position
        list_bitstreams[positions_remaining[next]] = bitstream

        # remove that position from those remaining
        positions_remaining.remove(positions_remaining[next])

    return list_bitstreams


def add_one(bin_value):
    """
    Convert a binary number to a bitstream of length "bit_count".
    """
    global character_count
    global bits_count

    # bin_value is an integer (but represented in binary)
    # so we can just add 1 to it
    bin_value = bin_value + 1
    # casting with bin converts it to a string with 0b in front
    binary = bin(bin_value)
    # get rid of the 0b at the front of the string
    bin_string = binary[2:]
    # pad the end with 0's if it isn't the desired length
    while len(bin_string) < bits_count:
        bin_string = '0' + bin_string

    # all done. return the bitstream (as a string)
    return bin_string


def store(bitstreams):
    """
    Convert a list of bitstreams to a dictionary.
    The KEYS are the characters in the set specified above.
    """
    global character_count
    global starting_character

    encode = {}
    char = starting_character
    for i in range(character_count):
        encode[char] = bitstreams[i]
        char = chr(ord(char) + 1)
    return encode


if __name__ == '__main__':
    bitstreams = make_bitstreams()
    encoder = store(bitstreams)
    print(encoder)
