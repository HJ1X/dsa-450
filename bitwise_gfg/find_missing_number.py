# Python 3

# You are given a list of n-1 integers and these integers are in the range of 1 to n. There are no duplicates
# in the list. One of the integers is missing in the list.

# Approaches:
# 1. Sort the array. loop from 1 to n - 1. check if i + 1 == arr[i]. print if not equal
# 2. Using sum equation. s = n(n+1)/2. s - sum(array) = miss_number. given below
# 3. Like 2nd approach, but adding and subtracting in every iteration to prevent overflow
# 4. Use XOR.


def find_miss_sum_eq(arr):
    n = len(arr) + 1
    sum_arr = n * (n + 1) // 2
    for i in range(n - 1):
        sum_arr -= arr[i]

    return sum_arr


def find_miss_sum_eq_prevent_overflow(arr):
    n = len(arr) + 1
    sum_arr = 1
    for i in range(1, n):
        sum_arr += i + 1
        sum_arr -= arr[i - 1]

    return sum_arr


def find_miss(arr):
    n = len(arr)
    sum_n = 0
    for i in range(n):
        sum_n += i+1
        sum_n -= arr[i]
    sum_n += n+1
    return sum_n


def find_miss_xor(arr):
    n = len(arr) + 1
    sum_arr = 1
    for i in range(1, n):
        sum_arr ^= i + 1              # adding 1 to go from 2 to n
        sum_arr ^= arr[i - 1]         # subtracting 1 to go from 0 to n-2 (0-based indexing)

    return sum_arr


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(find_miss_xor(arr))
    print(find_miss(arr))