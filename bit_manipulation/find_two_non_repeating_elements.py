# Python 3

# Given an array in which all numbers except two are repeated once. (i.e. we have 2n+2 numbers and n numbers are
# occurring twice and remaining two have occurred once). Find those two numbers

# Approaches
# 1. Sort elements and then check for adjacent elements if they are repeating while traversing the array.
# 2. Use maps to create count array.                                                        O(N) and O(N)
# 3. Use hash set. If element is already present remove it else add it to the set.          O(N) and O(N)
# 4. Use XOR. given below                                                                   O(N) and O(1)


def find_numbers(nums):
    xor = 0

    for ele in nums:
        xor ^= ele

    mask = xor & -xor

    num1 = 0
    num2 = 0

    for ele in nums:
        if ele & mask > 0:
            num1 ^= ele
        else:
            num2 ^= ele

    return min(num1, num2), max(num1, num2)


def find_non_repeating_using_xor(arr):
    n = len(arr)                     # Ex:- arr = [2, 4, 7, 9, 2, 4]
    sum_arr = 0

    # finding the xor of numbers which are not repeating Ex. xor of 7 and 9 = 14 (1110)
    for i in range(n):
        sum_arr ^= arr[i]

    # finding rightmost set bit of the sum_arr -> sum_arr & ~(sum_arr-1)   Ex. 1110 & ~(1101) = 0010 = 2
    sum_arr = sum_arr & -sum_arr

    num1 = 0
    num2 = 0

    # Dividing array in two sets, one with set bit = sum_arr and other with not equal.
    for i in range(n):
        if arr[i] & sum_arr > 0:
            num1 ^= arr[i]             # only element with set bit will be left and repeating element will be cancelled
        else:
            num2 ^= arr[i]             # only element with set bit not set will be left

    return min(num1, num2), max(num1, num2)


def main():
    arr = list(map(int, input().split()))
    print(*find_non_repeating_using_xor(arr))


if __name__ == '__main__':
    main()
