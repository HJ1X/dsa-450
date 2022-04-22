def python_slice(arr):
    return arr[::-1]


def reverse_recursive(arr, start, end):
    if start >= end:
        return arr
    arr[start], arr[end] = arr[end], arr[start]
    return reverse_recursive(arr, start + 1, end - 1)


def reverse_array_no_extra_space(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1
    return arr


def reverse_array(arr):
    rev_arr = []
    for i in range(len(arr)-1, -1, -1):
        rev_arr.append(arr[i])
    return ''.join(rev_arr)


arr = list(map(int, input().split()))
# arr = input()
start, end = 2, len(arr) - 1
# print(reverse_recursive(arr, start, end))
print(python_slice(arr))
