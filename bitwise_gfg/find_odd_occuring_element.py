# Python 3

# In the given array all the elements are occuring even number of times except one, which is occuring odd number of
# times. Find that element

# Approaches
# 1. for every element i check the count of number by iterating.
# 2. sort the elements and check for count in adjacent elements
# 3. use hashing or create a count array and check for odd count
# 4. Use xor. given below


def find_odd(arr):
    res = 0
    for i in range(len(arr)):
        res ^= arr[i]

    return res


def main():
    arr = list(map(int, input().split()))
    print(find_odd(arr))


if __name__ == '__main__':
    main()
