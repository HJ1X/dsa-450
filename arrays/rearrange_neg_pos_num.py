# python 3

# Rearrange numbers in negatives first and positive after them fashion but preserving their order in the array. Like
# stable sort.

def rearrange(n, arr):
    for i in range(n - 1):
        if arr[i] >= 0:
            continue

        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] >= 0:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key

    return arr


def merge(arr1, arr2):
    res = []

    i, j = 0, 0
    while i < len(arr1) and arr1[i] < 0:
        res.append(arr1[i])
        i += 1

    while j < len(arr2) and arr2[j] < 0:
        res.append(arr2[j])
        j += 1

    while i < len(arr1):
        res.append(arr1[i])
        i += 1

    while j < len(arr2):
        res.append(arr2[j])
        j += 1

    return res


def merge_sort_rearrange(arr, l, r):
    if l >= r:
        return [arr[l]]

    mid = (l + r) // 2

    arr1 = merge_sort_rearrange(arr, l, mid)
    arr2 = merge_sort_rearrange(arr, mid + 1, r)

    arr = merge(arr1, arr2)
    return arr


def reverse(arr, l, r):
    while l <= r:
        arr[l], arr[r] = arr[r], arr[l]
        l += 1
        r -= 1

    return


def merge_inplace(arr, l, m, r):
    # ptr1 will point to first occurrence of positive element in first array
    ptr1 = l
    ptr2 = m + 1

    while ptr1 <= m and arr[ptr1] < 0:
        ptr1 += 1

    while ptr2 <= r and arr[ptr2] < 0:
        ptr2 += 1

    reverse(arr, ptr1, m)
    reverse(arr, m + 1, ptr2 - 1)
    reverse(arr, ptr1, ptr2 - 1)

    return


def merge_sort_rearrange_inplace(arr, l, r):
    if l >= r:
        return

    mid = (l + r) // 2

    merge_sort_rearrange_inplace(arr, l, mid)
    merge_sort_rearrange_inplace(arr, mid + 1, r)

    merge_inplace(arr, l, mid, r)


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    # rearrange(n, arr)
    # arr = merge_sort_rearrange(arr, 0, len(arr)-1)
    merge_sort_rearrange_inplace(arr, 0, len(arr)-1)
    print(arr)


if __name__ == '__main__':
    main()
