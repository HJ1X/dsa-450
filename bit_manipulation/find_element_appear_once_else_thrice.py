# Python 3

# Given an array where every element occurs three times, except one element which occurs only once. Find the element
# that occurs once. The expected time complexity is O(n) and O(1) extra space.
import sys
INT_SIZE = 32


def find_element_gfg(arr):
    # this approach is not clear.

    n = len(arr)
    ones = 0
    twos = 0

    for i in range(n):
        # one & arr[i]" gives the bits that
        # are there in both 'ones' and new
        # element from arr[]. We add these
        # bits to 'twos' using bitwise XOR
        twos = twos ^ (ones & arr[i])

        # one & arr[i]" gives the bits that
        # are there in both 'ones' and new
        # element from arr[]. We add these
        # bits to 'twos' using bitwise XOR
        ones = ones ^ arr[i]

        # The common bits are those bits
        # which appear third time. So these
        # bits should not be there in both
        # 'ones' and 'twos'. common_bit_mask
        # contains all these bits as 0, so
        # that the bits can be removed from
        # 'ones' and 'twos'
        common_bit_mask = ~(ones & twos)

        # Remove common bits (the bits that
        # appear third time) from 'ones'
        ones &= common_bit_mask

        # Remove common bits (the bits that
        # appear third time) from 'twos'
        twos &= common_bit_mask
    return ones


def find_element_every_bit(arr):
    # TC - O(32N) and also not work for negative numbers

    # Initialize result
    result = 0
    n = len(arr)
    # Iterate through every bit
    for i in range(0, INT_SIZE):
        # Find sum of set bits at ith position in all array elements
        sm = 0
        x = (1 << i)
        for j in range(0, n):
            if arr[j] & x:
                sm = sm + 1
        # The bits with sum not multiple of 3, are the bits of element with single occurrence.
        if (sm % 3) != 0:
            result = result | x
    return result


def find_element(arr):
    three_n = sys.maxsize
    three_n_plus_1, three_n_plus_2 = 0, 0

    for i in range(len(arr)):
        common_3n = three_n & arr[i]
        common_3n_plus_1 = three_n_plus_1 & arr[i]
        common_3n_plus_2 = three_n_plus_2 & arr[i]

        three_n = three_n & ~common_3n
        three_n_plus_1 = three_n_plus_1 | common_3n

        three_n_plus_1 = three_n_plus_1 & ~common_3n_plus_1
        three_n_plus_2 = three_n_plus_2 | common_3n_plus_1

        three_n_plus_2 = three_n_plus_2 & ~common_3n_plus_2
        three_n = three_n | common_3n_plus_2

    return three_n_plus_1


def main():
    arr = list(map(int, input().split()))
    print(find_element_every_bit(arr))


if __name__ == '__main__':
    main()
