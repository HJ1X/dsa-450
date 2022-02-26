# python 3

# Find max element in a rotated sorted array

def find_max(arr):
    n = len(arr)
    low, high = 0, n-1

    while low < high:
        mid = (low + high) // 2
        if arr[high] < arr[mid]:
            low = mid + 1
        else:
            high = mid

    return arr[low]


def find_max_binary_search(arr):
    n = len(arr)
    low = 0
    high = n-1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid

    return arr[low-1]


def main():
    arr = [7, 8, 9, 10, 11, 1, 2, 3, 4, 5, 6]
    print(find_max(arr))
    print(find_max_binary_search(arr))


if __name__ == '__main__':
    main()
