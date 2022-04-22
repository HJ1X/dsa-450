# python 3

# LINTCODE 659

def encode(strs):
    encoded_string = ''

    # Encoding string by adding word length in front of word with '$' delimiter
    for string in strs:
        string_len = str(len(string))
        encoded_string += string_len + '$' + string

    return encoded_string


def decode(encoded_string):
    decoded_list = []
    i = 0
    while i < len(encoded_string):
        # Extracting word length
        j = i
        while encoded_string[j] != '$':
            j += 1
        curr_len = int(encoded_string[i: j])

        i = j + 1

        # Extracting actual word using curr_len
        curr_string = encoded_string[i: curr_len + i]

        decoded_list.append(curr_string)
        i += curr_len

    return decoded_list


def main():
    string_arr = input().split()

    encoded_string = encode(string_arr)
    decoded_arr = decode(encoded_string)

    if string_arr == decoded_arr:
        print(True)
    else:
        print(False)


if __name__ == '__main__':
    main()
