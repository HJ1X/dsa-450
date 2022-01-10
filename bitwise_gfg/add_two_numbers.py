# Python 3

# Write a function Add() that returns sum of two integers. The function should not use any of the arithmetic
# operators (+, ++, –, -, .. etc). Sum of two bits can be obtained by performing XOR (^) of the two bits. Carry bit
# can be obtained by performing AND (&) of two bits.

def sum_using_xor(x, y):
    while y != 0:
        carry = (x & y) << 1
        x = x ^ y
        y = carry
    return x


def sum_using_cor_recursive(x, y):
    if y == 0:
        return x
    sums = x ^ y
    carry = (x & y) << 1
    # return sum_using_cor_recursive(x ^ y, (x & y) << 1)
    return sum_using_cor_recursive(sums, carry)


def main():
    x, y = map(int, input().split())
    print(sum_using_cor_recursive(x, y))


if __name__ == '__main__':
    main()
