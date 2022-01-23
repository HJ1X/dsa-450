# python 3

def find_peak(arr, l, r):
    mid = (l + r) // 2
    # if mid - 1 < 0:
    #     return max(arr[mid], arr[mid+1])
    #
    # if mid + 1 > r:
    #     # Although only returning arr[mid] is correct because this condition would only happen when l == r on last
    #     # element
    #     return max(arr[mid], arr[mid - 1])

    if mid - 1 >= 0 and arr[mid - 1] > arr[mid]:
        return find_peak(arr, l, mid - 1)

    elif mid + 1 <= r and arr[mid + 1] > arr[mid]:
        return find_peak(arr, mid + 1, r)

    else:
        return arr[mid]


def main():
    arr = list(map(int, input().split()))
    print(find_peak(arr, 0, len(arr) - 1))


if __name__ == '__main__':
    main()
