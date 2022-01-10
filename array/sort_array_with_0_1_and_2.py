def sort012(arr, n):
    # code here

    ptr_1, ptr_2 = 0, 0

    for i in range(n):
        if arr[i] == 0:
            arr[i], arr[ptr_1] = arr[ptr_1], arr[i]
            ptr_1 += 1
            if ptr_2 < ptr_1: ptr_2 = ptr_1
        if arr[i] == 1:
            arr[i], arr[ptr_2] = arr[ptr_2], arr[i]
            ptr_2 += 1

    return arr


def sort012_dutch_national_flag(arr, n):
    #  Correct code    three pointer approach
    # low, mid = 0, 0
    # high = n - 1
    #
    # while mid <= high:
    #     if arr[mid] == 0:
    #         arr[low], arr[mid] = arr[mid], arr[low]
    #         low += 1
    #         mid += 1
    #     elif arr[mid] == 1:
    #         mid += 1
    #     else:
    #         arr[mid], arr[high] = arr[high], arr[mid]
    #         high -= 1
    # return arr

    # two iteration approach. From i to k which sorts 0 and then from n - 1 to l (step -1) which sorts 2. middle
    # elements then remain 1.

    ptr = 0
    for i in range(n):
        if arr[i] == 0:
            arr[i], arr[ptr] = arr[ptr], arr[i]
            ptr += 1

    ptr_2 = n - 1
    for i in range(n - 1, ptr - 1, -1):
        if arr[i] == 2:
            arr[i], arr[ptr_2] = arr[ptr_2], arr[i]
            ptr_2 -= 1

    return arr


lst = list(map(int, input().split()))
print(sort012(lst, len(lst)))