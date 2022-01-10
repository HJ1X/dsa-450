# Python 3

# Given two numbers ‘a’ and b’. Write a program to count number of bits needed to be flipped to convert ‘a’ to ‘b’.

# Approaches
# 1. Calculate xor of a and b. Calculate number of set bits in a and b.
# 2. while a and b are not equal to 0, calculate value of rightmost bit. if different add to count else not.

def count_flip_bits_direct(a, b):
    flips = 0
    while a > 0 or b > 0:
        bit1 = a & 1
        bit2 = b & 1
        if bit1 != bit2:
            flips += 1
        a >>= 1
        b >>= 1
    return flips


def count_flip_bits(a, b):
    xor = a ^ b

    # count no. of set bits in xor
    # count = 0
    # while xor:
    #     count += xor & 1
    #     xor >>= 1

    # another method to count set bits
    count = 0
    while xor:
        count += 1
        xor &= (xor - 1)

    return count


def main():
    a, b = map(int, input().split())
    print(count_flip_bits_direct(a, b))


if __name__ == '__main__':
    main()
