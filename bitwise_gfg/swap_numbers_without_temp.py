# Python 3

# approaches
# 1. By using sum. given below


def swap_sum(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b


def swap_prod(a, b):         # Cannot be used if one value is 0
    a = a * b
    b = a // b
    a = a // b
    return a, b


def swap_xor(a, b):
    # All the approaches fail when the pointers are passed as arguments and they point to the same variable. SO, this
    # condition is used. Suppose if we are passing elements of list x[i], y[i], then return if their addresses are same
    if a == b:
        return
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b


def main():
    a, b = list(map(int, input().split()))
    print(*swap_xor(a, b))


if __name__ == '__main__':
    main()
