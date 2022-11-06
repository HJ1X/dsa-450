# Python 3

def find_high(arr, key, l, r):
    if l > r:
        return r
    mid = (l + r) // 2
    if arr[mid] <= key:
        return find_high(arr, key, mid + 1, r)
    else:
        return find_high(arr, key, l, mid - 1)


def find_low(arr, key, l, r):
    if l > r:
        if arr[l] == key:
            return l
        return -1

    mid = (l+r) // 2
    if arr[mid] < key:
        return find_low(arr, key, mid + 1, r)
    else:
        return find_low(arr, key, l, mid - 1)


def find_low_high(arr, key):
    low = find_low(arr, key, 0, len(arr) - 1)
    if low != -1:
        high = find_high(arr, key, 0, len(arr) - 1)
        return low, high
    return -1, -1


def find_extreme(arr, n, target, find_left):
    low = 0
    high = n - 1
    i = -1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] < target:
            low = mid + 1
        elif arr[mid] > target:
            high = mid - 1

        else:
            i = mid
            if find_left:
                high = mid - 1
            else:
                low = mid + 1

    return i


n = int(input())
l = int(input())
arr = []
for i in range(n):
    arr.append(int(input()))

arr.sort()
left = find_extreme(arr, n, l, True)
right = find_extreme(arr, n, l, False)

if left == -1:
    print('Not found')
else:
    print(left, right)


def find(arr, n, x):
    left = find_extreme(arr, n, x, True)
    right = find_extreme(arr, n, x, False)
    return left, right


def main():
    n, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(*find_low_high(arr, x))


if __name__ == '__main__':
    main()