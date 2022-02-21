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

    return arr[low - 1]


def main():
    arr = [6, 1, 2, 3, 4, 5]
    print(find_max(arr))


if __name__ == '__main__':
    main()
