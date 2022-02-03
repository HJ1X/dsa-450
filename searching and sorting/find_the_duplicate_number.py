# Python 3

# Floyd cycle detection algorithm (Tortoise method) | leetcode - 287

# 1st approach is by mutating array, i.e.
# by using approach of marking visited elements as -1 (find_repeating_and_missing.py)

# 2nd approach can be used when array cannot be modified. Given below:-

def find_duplicate_negatives(arr):
    n = len(arr)

    # For every element in array, marking arr[element] negative.
    for i in range(n):
        index = abs(arr[i])     # Taking abs value as elements could be -ve
        arr[index] *= -1

    # Checking for positive number from 1st index because range is between 1 to n.
    for i in range(1, n):
        if arr[i] > 0:
            return i


def find_duplicate(arr):
    n = len(arr)
    slow, fast = arr[0], arr[0]

    # Initially iterating them once
    slow = arr[slow]
    fast = arr[arr[fast]]

    # Looping until slow and fast collide
    while slow != fast:
        slow = arr[slow]
        fast = arr[arr[fast]]

    slow = arr[0]

    # Looping for second collision to find duplicate i.e. starting node of cycle.
    while slow != fast:
        slow = arr[slow]
        fast = arr[fast]

    return slow


def main():
    arr = list(map(int, input().split()))
    # print(find_duplicate(arr))
    print(find_duplicate_negatives(arr))


if __name__ == '__main__':
    main()
