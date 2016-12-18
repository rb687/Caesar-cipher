

alphabet_list = ['A', 'B', 'C', 'D', 'E',
                 'F', 'G', 'H', 'I', 'J',
                 'K', 'L', 'M', 'N', 'O',
                 'P', 'Q', 'R', 'S', 'T',
                 'U', 'V', 'W', 'X', 'Y',
                 'Z' ]

alphabet_list_len = len(alphabet_list)


def calc_shift(shiftBy):
    i = None
    if shiftBy >= 0:
        i = shiftBy
    else:
        i = shiftBy + alphabet_list

    return i

def encrypt(shiftBy, message):
    shifted_letter_index = calc_shift(shiftBy)
    encrypted_msg = ''

    for letter in message:
        letter_index = alphabet_list.index(letter)
        shifted_index = letter_index + shifted_letter_index
        encrypted_msg += alphabet_list[shifted_index]

    return encrypted_msg


def decrypt(message, shiftBy):
    shifted_letter_index = calc_shift(shiftBy)
    decrypted_msg = ''

    for letter in message:



