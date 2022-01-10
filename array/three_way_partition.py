# python 3

# partition arr in three parts | https://practice.geeksforgeeks.org/problems/three-way-partitioning/1

# Given an array of size n and a range [a, b]. The task is to partition the array around the range such that array is
# divided into three parts.
# 1) All elements smaller than a come first.
# 2) All elements in range a to b come next.
# 3) All elements greater than b appear in the end.
# The individual elements of three sets can appear in any order. You are required to return the modified array.


def partition(arr, n, a, b):
    n = len(arr)
    ptr1, ptr2 = -1, -1
    i = 0
    while i < n:
        if ptr1 + 1 < n and arr[i] < a:
            ptr1 += 1
            arr[i], arr[ptr1] = arr[ptr1], arr[i]
            if ptr2 < ptr1:
                ptr2 = ptr1

        if ptr2 + 1 < n and a <= arr[i] <= b:
            ptr2 += 1
            arr[i], arr[ptr2] = arr[ptr2], arr[i]

        i += 1
    return arr


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    a, b = map(int, input().split())
    print(partition(arr, n, a, b))


if __name__ == '__main__':
    main()
