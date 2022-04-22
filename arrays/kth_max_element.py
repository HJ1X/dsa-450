# python 3

from random import randint
from typing import List


def partition(arr, low, high):
    idx = randint(low, high)
    pivot = arr[idx]
    arr[idx], arr[low] = arr[low], arr[idx]
    j = low
    for i in range(j + 1, high + 1):
        if arr[i] <= pivot:
            j += 1
            arr[i], arr[j] = arr[j], arr[i]

    arr[j], arr[low] = arr[low], arr[j]
    return j


def find_kth_largest(nums: List[int], k: int) -> int:
    arr = nums
    n = len(arr)
    k = n - k

    low, high = 0, n - 1
    while low <= high:
        index_partition = partition(arr, low, high)

        if index_partition == k:
            return arr[k]

        if index_partition < k:
            low = index_partition + 1
        else:
            high = index_partition - 1

    return -1


def main():
    arr = [3, 2, 1, 5, 6, 4]
    k = 2
    print(find_kth_largest(arr, k))


if __name__ == '__main__':
    main()
