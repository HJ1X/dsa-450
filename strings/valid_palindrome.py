# python 3

def is_valid_palindrome(string):
    # Creating alpha_numeric set
    numbers = [str(i) for i in range(10)]

    start = ord('a')
    letters = [chr(i) for i in range(start, start + 26)]

    alpha_numeric_chars = set(numbers + letters)

    # Checking if palindrome
    i, j = 0, len(string) - 1

    while i != j:
        if string[i].lower() not in alpha_numeric_chars:
            i += 1
            continue

        if string[j].lower() not in alpha_numeric_chars:
            j -= 1
            continue

        if string[i].lower() != string[j].lower():
            return False

        i += 1
        j -= 1

    return True


def main():
    string = "A man, a plan, a canal: Panama"
    print(is_valid_palindrome(string))


if __name__ == '__main__':
    main()
