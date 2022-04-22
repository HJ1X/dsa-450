# python 3


def merge_count(arr_left, arr_right):
    i, j = 0, 0
    n, m = len(arr_left), len(arr_right)

    inv_count = 0
    merged_arr = []

    while i < n and j < m:
        if arr_left[i] <= arr_right[j]:
            merged_arr.append(arr_left[i])
            i += 1

        else:
            merged_arr.append(arr_right[j])
            inv_count += n - i
            j += 1

    while i < n:
        merged_arr.append(arr_left[i])
        i += 1

    while j < m:
        merged_arr.append(arr_right[j])
        j += 1

    return inv_count, merged_arr


def count_inversion(arr, low, high):
    if low >= high:
        return 0, [arr[low]]

    mid = (low + high) // 2

    count_left, arr_left = count_inversion(arr, low, mid)
    count_right, arr_right = count_inversion(arr, mid + 1, high)

    count_merge, merged_arr = merge_count(arr_left, arr_right)

    inv_count = count_left + count_right + count_merge
    return inv_count, merged_arr


# ----- we can either use j as inv_count or n - i as inv_count as in below and above approach ----------- #

def merge(arr1, arr2):
    i, j = 0, 0

    temp_arr = []
    inv_count = 0
    while i < len(arr1) and j < len(arr2):
        if arr1[i] <= arr2[j]:
            temp_arr.append(arr1[i])
            i += 1

        else:
            temp_arr.append(arr2[j])
            inv_count += j + 1
            j += 1

    while i < len(arr1):
        temp_arr.append(arr1[i])
        inv_count += j
        i += 1

    while j < len(arr2):
        temp_arr.append(arr2[j])
        j += 1

    return inv_count, temp_arr


def merge_sort(arr, l, r):
    if l >= r:
        return 0, [arr[l]]

    inv_count = 0
    mid = (l + r) // 2

    inv_count1, arr1 = merge_sort(arr, l, mid)
    inv_count2, arr2 = merge_sort(arr, mid + 1, r)

    inv_count3, arr = merge(arr1, arr2)

    inv_count = inv_count1 + inv_count2 + inv_count3
    return inv_count, arr


def merge_temp(arr, low, mid, high):
    i, j = low, mid + 1
    temp = []
    inv_count = 0

    while i <= mid and j <= high:
        if arr[i] <= arr[j]:
            temp.append(arr[i])
            i += 1

        else:
            temp.append(arr[j])
            inv_count += mid - i + 1
            j += 1

    while i <= mid:
        temp.append(arr[i])
        i += 1

    while j <= high:
        temp.append(arr[j])
        j += 1

    for i in range(low, high + 1):
        arr[i] = temp[i - low]

    return inv_count


def count_inversion_temp(arr, low, high):
    if low >= high:
        return 0

    inv_count = 0
    mid = (low + high) // 2

    inv_count += count_inversion(arr, low, mid)
    inv_count += count_inversion(arr, mid + 1, high)

    inv_count += merge_temp(arr, low, mid, high)

    return inv_count


def inversion_count(arr, n):
    return merge_sort(arr, 0, n - 1)[0]


def main():
    arr = list(map(int, input().split()))
    print(inversion_count(arr, len(arr)))


if __name__ == '__main__':
    main()
