# python 3
from math import log10, floor
from random import randint

# Q. Why Quick Sort is preferred over MergeSort for sorting Arrays ?
# Quick Sort in its general form is an in-place sort ( i.e. it doesn’t require any extra storage) whereas merge sort
# requires O(N) extra storage, N denoting the array size which may be quite expensive. Allocating and de-allocating
# the extra space used for merge sort increases the running time of the algorithm. Comparing average complexity we
# find that both type of sorts have O(NlogN) average complexity but the constants differ. For arrays, merge sort
# loses due to the use of extra O(N) storage space. Most practical implementations of Quick Sort use randomized
# version. The randomized version has expected time complexity of O(nLogn). The worst case is possible in randomized
# version also, but worst case doesn’t occur for a particular pattern (like sorted array) and randomized Quick Sort
# works well in practice. Quick Sort is also a cache friendly sorting algorithm as it has good locality of reference
# when used for arrays. Quick Sort is also tail recursive, therefore tail call optimizations is done.
#
#
#
# Q. Why MergeSort is preferred over QuickSort for Linked Lists?
# In case of linked lists the case is different mainly due to difference in memory allocation of arrays and linked
# lists. Unlike arrays, linked list nodes may not be adjacent in memory. Unlike array, in linked list, we can insert
# items in the middle in O(1) extra space and O(1) time. Therefore merge operation of merge sort can be implemented
# without extra space for linked lists. In arrays, we can do random access as elements are continuous in memory. Let
# us say we have an integer (4-byte) array A and let the address of A[0] be x then to access A[i], we can directly
# access the memory at (x + i*4). Unlike arrays, we can not do random access in linked list. Quick Sort requires a
# lot of this kind of access. In linked list to access i’th index, we have to travel each and every node from the
# head to i’th node as we don’t have continuous block of memory. Therefore, the overhead increases for quick sort.
# Merge sort accesses data sequentially and the need of random access is low.


def shell_sort(arr):
    # Better implementation on oneNote
    # Shell sort works on concept of insertion sort, with gap introduced to reduce number of swaps in
    # reverse sorted arrays and similar

    n = len(arr)
    gap = n // 2

    # Decrementing value of gap from n to 0 by a factor of 2 (Could be improved)
    while gap > 0:
        j = gap
        # Incrementing value of j from gap to n. Iterating array for every value of gap
        while j < n:
            i = j - gap
            # Decrementing i from j - gap to 0 to insert value at j in correct position in subarray [j:-1:-gap]
            while i >= 0:
                if arr[i] <= arr[i + gap]:
                    break            # break if arr[j] is already at correct position
                arr[i], arr[i + gap] = arr[i + gap], arr[i]
                i -= gap
            j += 1
        gap //= 2

    return arr


def bucket_sort(arr):
    # Bucket sort should be implemented considering the input range
    # a good choice for number of buckets could be the square root of range

    # This implementation is just for numbers between 0.01 to 0.99

    # min_element, max_element = min(arr), max(arr)
    # element_range = max_element - min_element
    # no_of_buckets = isqrt(element_range) + 1

    bucket_arr = [[] for i in range(10)]

    # Put elements in buckets
    for element in arr:
        bucket_choice = int(element * 10)
        bucket_arr[bucket_choice].append(element)

    # Sort individual buckets
    for i in range(len(bucket_arr)):
        bucket_arr[i] = quick_sort_equal_elements(bucket_arr[i], 0, len(bucket_arr[i]) - 1)

    arr = []
    # Concatenating array
    for i in range(len(bucket_arr)):
        if bucket_arr[i]:
            for element in bucket_arr[i]:
                arr.append(element)

    return arr


def radix_sort(arr):
    max_digit = int(log10(max(arr))) + 1

    for digit in range(max_digit):
        count_bucket = [[] for i in range(10)]

        for num in arr:
            temp = num
            temp //= 10 ** digit        # 1482 // 10**2 = 14
            digit_val = temp % 10       # 14 % 10 = 4, which is the digit_val (index) for count_bucket

            count_bucket[digit_val].append(num)

        i = 0
        j = 0
        while i < len(arr):
            if count_bucket[j]:
                for ele in count_bucket[j]:
                    arr[i] = ele
                    i += 1
            j += 1

    return arr


def counting_sort(arr):
    k = max(arr)
    count = [0 for i in range(k+1)]

    for ele in arr:
        count[ele] += 1

    j = 0
    i = 0

    while i < len(arr):
        if count[j] > 0:
            arr[i] = j
            count[j] -= 1
        else:
            while count[j] == 0:
                j += 1
            i -= 1
        i += 1

    return arr


def counting_sort_standard(arr):
    k = max(arr)
    count = [0 for i in range(k + 1)]

    for ele in arr:
        count[ele] += 1

    # Count will now store actual position of elements
    for i in range(1, k+1):
        count[i] += count[i-1]

    output_arr = [-1 for i in range(len(arr))]
    for i in range(len(arr)):
        key = arr[i]
        output_arr[count[key]-1] = key
        count[key] -= 1

    return output_arr


def partition_equal_elements(arr, l, r):
    pivot = randint(l, r)
    key = arr[pivot]
    j, k = l, l
    arr[pivot], arr[j] = arr[j], arr[pivot]
    for i in range(l + 1, r + 1):
        if arr[i] < key:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
            if k < j:
                k = j
        if arr[i] == key:
            k += 1
            arr[k], arr[i] = arr[i], arr[k]
    arr[j], arr[l] = arr[l], arr[j]
    return j, k


def quick_sort_equal_elements(arr, l, r):
    if l > r:
        return

    m1, m2 = partition_equal_elements(arr, l, r)
    quick_sort_equal_elements(arr, l, m1 - 1)
    quick_sort_equal_elements(arr, m2 + 1, r)

    return arr


def partition(arr, l, r):
    pivot = randint(l, r)
    key = arr[pivot]
    j = l
    arr[pivot], arr[j] = arr[j], arr[pivot]
    for i in range(l + 1, r + 1):
        if arr[i] <= key:
            j += 1
            arr[j], arr[i] = arr[i], arr[j]
    arr[j], arr[l] = arr[l], arr[j]
    return j


def quick_sort(arr, l, r):
    if l > r:
        return

    m = partition(arr, l, r)
    quick_sort(arr, l, m - 1)
    quick_sort(arr, m + 1, r)

    return arr


def merge(arr1, arr2):
    i, j = 0, 0
    sorted_arr = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            sorted_arr.append(arr1[i])
            i += 1
        else:
            sorted_arr.append(arr2[j])
            j += 1
    while i < len(arr1):
        sorted_arr.append(arr1[i])
        i += 1
    while j < len(arr2):
        sorted_arr.append(arr2[j])
        j += 1
    return sorted_arr


def merge_sort(arr, l, r):
    if l >= r:
        return [arr[l]]

    mid = (l + r) // 2
    arr1 = merge_sort(arr, l, mid)
    arr2 = merge_sort(arr, mid + 1, r)

    return merge(arr1, arr2)


def insertion_sort(arr):
    for i in range(1, len(arr)):
        curr_element = arr[i]
        j = i - 1
        while j >= 0 and curr_element < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = curr_element
    return arr


def bubble_sort(arr):
    for i in range(len(arr)):
        swapped = False
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                swapped = True
        if not swapped:
            break
    return arr


def selection_sort(arr):
    for i in range(len(arr)):
        min_index = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_index]:
                min_index = j
        arr[i], arr[min_index] = arr[min_index], arr[i]
    return arr


def main():
    arr = list(map(int, input().split()))
    # print(*insertion_sort(arr))
    # print(*quick_sort_equal_elements(arr, 0, len(arr) - 1))
    # print(shell_sort(arr))
    # print(quick_sort(arr, 0, len(arr) - 1))
    # print(counting_sort_standard(arr))
    print(radix_sort(arr))


if __name__ == '__main__':
    main()
