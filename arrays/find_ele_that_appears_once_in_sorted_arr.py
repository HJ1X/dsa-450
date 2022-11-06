# python 3

def find_once(arr, n):
    low, high = 0, n - 1
    while low <= high:
        mid = (low + high) // 2

        if mid % 2 == 0:
            if arr[mid + 1] == arr[mid]:
                low = mid + 1
            else:
                high = mid - 1

        else:
            if arr[mid + 1] == arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

    return arr[low]


def main():
    arr = list(map(int, input().split()))
    print(find_once(arr, len(arr)))


if __name__ == '__main__':
    main()
