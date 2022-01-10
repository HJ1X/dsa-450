def find_min_and_max(arr):
    min, max = arr[0], arr[0]
    for ele in arr:
        if ele > max:
            max = ele
            continue
        if ele < min:
            min = ele
    return max, min


def find_min_max_divide_and_conquer(arr, start, end):
    if start >= end:
        return arr[start], arr[start]

    mid = (start + end) // 2
    left_min_val, left_max_val = find_min_max_divide_and_conquer(arr, start, mid)
    right_min_val, right_max_val = find_min_max_divide_and_conquer(arr, mid + 1, end)

    return min(left_min_val, right_min_val), max(left_max_val, right_max_val)


arr = list(map(int, input().split()))
# print(find_min_and_max(arr))
print(find_min_max_divide_and_conquer(arr, 0, len(arr) - 1))