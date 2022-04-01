# Python 3

# Given two signed integers, write a function that returns true if the signs of given integers are different,
# otherwise false. The function should not use any of the arithmetic operators.

def check_sign(a, b):
    # if a ^ b < 0:
    #     return True
    # return False

    # or

    return b >= 0 if a < 0 else b < 0

    # or

    # if a < 0:
    #     return b >= 0
    # else:
    #     return b < 0


def main():
    a, b = map(int, input().split())
    print(check_sign(a, b))


if __name__ == '__main__':
    main()