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


def main():
    n, x = list(map(int, input().split()))
    arr = list(map(int, input().split()))
    print(*find_low_high(arr, x))


if __name__ == '__main__':
    main()