# python 3

import math

# In this problem, given two sorted arrays of length n and m, merge them as two sorted arrays i.e.
# 1st array will be containing elements from 1 to n and second from n + 1 to n + m in sorted fashion

# Three approaches could be used:
# 1. Create array of size n + m. Insert all elements. Sort this array. At last, fill arr1 and arr2 from this array
#       TC - O(NlogN) + O(N) + O(N)         SC - O(N + M)
# 2. Using insertion sort approach. iterate arr1 with i. For every i, iterate j in arr2. If arr[i] > arr[j], then
#    swap elements and insert element at arr[j] in correct position in arr2. Increment i.
#       TC - O(n * m)                       SC - O(1)
# 3. Using shell sort approach.
#       TC - O(NlogN)                       SC - O(1)


# ----------------------------------------------------- GFG CODE ----------------------------------------------------- #
def merge_gfg(ar1, ar2):
    m = len(ar1)
    n = len(ar2)
    # Iterate through all
    # elements of ar2[] starting from
    # the last element
    for i in range(n - 1, -1, -1):

        # Find the smallest element
        # greater than ar2[i]. Move all
        # elements one position ahead
        # till the smallest greater
        # element is not found
        last = ar1[m - 1]
        j = m - 2
        while j >= 0 and ar1[j] > ar2[i]:
            ar1[j + 1] = ar1[j]
            j -= 1

        # If there was a greater element
        if j != m - 2 or last > ar2[i]:
            ar1[j + 1] = ar2[i]
            ar2[i] = last
    return ar1, ar2


def merge_gfg_2(arr1, arr2):
    i, j, k = 0, 0, len(arr1)-1
    while i <= k and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        else:
            arr2[j], arr1[k] = arr1[k], arr2[j]
            k -= 1
            j += 1
    arr1.sort()
    arr2.sort()
    return arr1, arr2


def next_gap(gap):
    if gap <= 1:
        return 0
    return (gap // 2) + (gap % 2)


def merge_gap_gfg(arr1, arr2, n, m):
    gap = n + m
    gap = next_gap(gap)
    while gap > 0:

        # comparing elements in
        # the first array.
        i = 0
        while i + gap < n:
            if arr1[i] > arr1[i + gap]:
                arr1[i], arr1[i + gap] = arr1[i + gap], arr1[i]

            i += 1

        # comparing elements in both arrays.
        j = gap - n if gap > n else 0
        while i < n and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]

            i += 1
            j += 1

        if j < m:
            # comparing elements in the
            # second array.
            j = 0
            while j + gap < m:
                if arr2[j] > arr2[j + gap]:
                    arr2[j], arr2[j + gap] = arr2[j + gap], arr2[j]

                j += 1

        gap = next_gap(gap)


# -------------------------------------------------------- MY CODE --------------------------------------------------- #
def merge_gap(arr1, arr2, n, m):
    gap = math.ceil((n + m) / 2)
    while gap > 0:
        i = 0
        # Traversing in 1st arr
        while i + gap < n:
            if arr1[i] > arr1[gap + i]:
                arr1[i], arr1[gap + i] = arr1[gap + i], arr1[i]
            i += 1

        # Traversing in 1st and 2nd arr
        j = (i + gap) - n
        while i < n and j < m:
            if arr1[i] > arr2[j]:
                arr1[i], arr2[j] = arr2[j], arr1[i]
            i += 1
            j += 1

        # Traversing in 2nd arr
        i = 0
        while i + gap < m:
            if arr2[i] > arr2[gap + i]:
                arr2[i], arr2[gap + i] = arr2[gap + i], arr2[i]
            i += 1

        gap = next_gap(gap)


def merge_insertion(arr1, arr2, n, m):
    i = 0
    while i < n:
        if arr1[i] > arr2[0]:
            # swap
            arr1[i], arr2[0] = arr2[0], arr1[i]

            # put arr2[0] at its correct pos
            j = 1
            val = arr2[0]
            while j < m and arr2[j] < val:
                arr2[j-1] = arr2[j]
                j += 1
            arr2[j-1] = val

        i += 1


def merge(arr1, arr2, n, m):
    i, j = n - 1, 0

    while i >= 0 and j < m and arr1[i] > arr2[j]:
        arr1[i], arr2[j] = arr2[j], arr1[i]
        i -= 1
        j += 1

    arr1.sort()
    arr2.sort()


def main():
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    # res1_arr, res2_arr = merge_gfg_2(arr1, arr2)
    # print(*res1_arr)
    # print(*res2_arr)
    # print(merge_insertion(arr1, arr2, len(arr1), len(arr2)))
    merge_gap_gfg(arr1, arr2, len(arr1), len(arr2))
    print(arr1, arr2)


if __name__ == '__main__':
    main()