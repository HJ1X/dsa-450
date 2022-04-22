# python 3

def find_peak(arr, l, r):
    mid = (l + r) // 2

    if mid - 1 >= l and arr[mid - 1] > arr[mid]:
        return find_peak(arr, l, mid - 1)

    elif mid + 1 <= r and arr[mid + 1] > arr[mid]:
        return find_peak(arr, mid + 1, r)

    else:
        return mid


def main():
    arr = list(map(int, input().split()))
    print(find_peak(arr, 0, len(arr) - 1))


if __name__ == '__main__':
    main()
