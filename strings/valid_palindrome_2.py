# python 3
# Leetcode 680

def is_palindrome(string, i, j):
    while i < j:
        if string[i] != string[j]:
            return False
        i += 1
        j -= 1

    return True


def is_valid_palindrome(string: str) -> bool:
    i, j = 0, len(string) - 1

    while i < j:
        if string[i] != string[j]:
            if (is_palindrome(string, i + 1, j) or
                is_palindrome(string, i, j - 1)
            ):
                return True

            else:
                return False

        i += 1
        j -= 1

    return True


def main():
    string = 'atbbga'
    print(is_valid_palindrome(string))


if __name__ == '__main__':
    main()
