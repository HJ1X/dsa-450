# python 3

def is_stretchy(stretchy_word, string):
    if not stretchy_word and string or not string and stretchy_word:
        return False

    if not stretchy_word and not string:
        return True

    i, j = 0, 0
    curr_char = stretchy_word[i]
    while i < len(stretchy_word) and stretchy_word[i] == curr_char:
        i += 1

    while j < len(string) and string[j] == curr_char:
        j += 1

    if i == j or j >= 3:
        return is_stretchy(stretchy_word[i:], string[j:])

    else:
        return False


def expressive_words(string, words):
    count = 0

    for word in words:
        if is_stretchy(word, string):
            count += 1

    return count


def main():
    string = 'abcd'  # input()
    words = ["abc"]    # input().split()
    print(expressive_words(string, words))


if __name__ == '__main__':
    main()
