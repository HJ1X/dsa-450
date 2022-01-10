def move_neg(arr, n):
    ptr = 0
    for i in range(n):
        if arr[i] < 0:
            arr[ptr], arr[i] = arr[i], arr[ptr]
            ptr += 1
    return arr


arr = list(map(int, input().split()))
print(move_neg(arr, len(arr)))