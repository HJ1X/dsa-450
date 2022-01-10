# Python 3

# Given a number x and two positions (from the right side) in the binary representation of x, write a function that
# swaps n bits at given two positions and returns the result. It is also given that the two sets of bits do not
# overlap. | GFG https://www.geeksforgeeks.org/swap-bits-in-a-given-number/

# Approaches:
# 1. Using xor operations given below
# 2. Using and operations and checking every bit till of n one by one. refer link

def swap_bits(x, p1, p2, n):
    # Ex. - n = 00101111      p1 = 1        p2 = 5         n = 3

    # Creating set1 of bits to be swapped. (1 << n) - 1 will set first n digits 1 and all others 0.
    # After performing & operation, n digits to be swapped are extracted.
    # Ex. - 00101111 >> 1 = 0010111,    (1 << 3) - 1 = 1000 - 1 -> 1000 - 1 = 111 (last three digits are 1)
    # finally,   0010111 & 111 = 111 = 7
    set1 = (x >> p1) & ((1 << n) - 1)

    # x. - 00101111 >> 5 = 001,    (1 << 3) - 1 = 1000 - 1 -> 1000 - 1 = 111 (last three digits are 1)
    # finally,   001 & 111 = 001 = 1
    set2 = (x >> p2) & ((1 << n) - 1)

    # performing xor on set1 and set2, will give a set which can be used to swap these two sets.
    # ex. 111 ^ 001 = 110      Now, 110 can be used to swap both numbers
    # 110 ^ 001 = 111  and  110 ^ 111 = 001,  i.e. numbers gets swapped as we use to swap two numbers
    set_xor = set1 ^ set2

    # placing xor_set at its correct values i.e. p1 and p2
    # Ex. - 110 << 1 = 1100       110 << 5 = 11000000
    # finally,   [110] | [110]00000 = [110]0[110]0
    # now, we have a set of digits on which performing xor with x will swap bits at p1 and p2 only. Rest will remain
    # unaffected as other bits are 0 and xor with 0 gives number itself, i.e. a ^ 0 = a
    set_swapper = (set_xor << p1) | (set_xor << p2)

    result = set_swapper ^ x
    return result


def main():
    x, p1, p2, n = map(int, input().split())
    print(swap_bits(x, p1, p2, n))


if __name__ == '__main__':
    main()
