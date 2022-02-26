from typing import List


def find_min_duplicates(arr: List[int]) -> int:
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            low = mid + 1

        elif arr[mid] < arr[high]:
            high = mid

        else:
            high -= 1

    return arr[low]


def find_min(arr: List[int]) -> int:
    low, high = 0, len(arr) - 1

    while low < high:
        mid = (low + high) // 2

        if arr[mid] > arr[high]:
            low = mid + 1
        else:
            high = mid

    return arr[low]


def main():
    # this function returns minimum index
    arr = list(map(int, input().split()))
    print(find_min(arr))


if __name__ == '__main__':
    main()
