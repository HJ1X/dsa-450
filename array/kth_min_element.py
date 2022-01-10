from random import randint


def kth_smallest(arr, l, r, k):
    '''
    arr : given array
    l : starting index of the array i.e 0
    r : ending index of the array i.e size-1
    k : find kth smallest element and return using this function
    '''

    min_indexes = []

    for i in range(k):
        min_index = -1
        for j in range(r + 1):
            if j not in min_indexes:
                min_index = j
                break

        for j in range(r + 1):
            if j not in min_indexes and arr[j] < arr[min_index]:
                min_index = j
        min_indexes.append(min_index)
    # print(min_indexes.pop())
    return arr[min_indexes.pop()]


def partition(arr, l, r):
    rand = randint(l, r)
    pivot = arr[rand]
    j = l
    for i in range(l, r):
        if arr[i] <= pivot:
            arr[i], arr[j] = arr[j], arr[i]
            j += 1
    arr[j], arr[rand] = arr[rand], arr[j]
    return j


def kth_smallest_quick_select(arr, l, r, k):
    index_after_partition = partition(arr, l, r)

    if k - 1 == index_after_partition:
        return arr[k - 1]
    if index_after_partition < k - 1:
        return kth_smallest_quick_select(arr, index_after_partition + 1, r, k)
    else:
        return kth_smallest_quick_select(arr, l, index_after_partition - 1, k)


arr = list(map(int, input().split()))
k = int(input())
# print(kth_smallest(arr, 0, len(arr) - 1, k))
print(kth_smallest_quick_select(arr, 0, len(arr) - 1, k))