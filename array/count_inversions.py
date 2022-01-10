# python 3

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


def inversion_count(arr, n):
    return merge_sort(arr, 0, n - 1)[0]


def main():
    arr = list(map(int, input().split()))
    print(inversion_count(arr, len(arr)))


if __name__ == '__main__':
    main()
