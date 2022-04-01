# python 3

def find_smaller(matrix, target):
    count = 0

    for row in matrix:
        low = 0
        high = len(row) - 1

        while low <= high:
            mid = (low + high) // 2

            if row[mid] <= target:
                low = mid + 1
            else:
                high = mid - 1

        count += low

    return count


def find_median(matrix, rows, cols):
    low = 0
    high = int(10e9)
    half = (rows * cols) // 2

    while low <= high:
        mid = (low + high) // 2

        smaller_numbers = find_smaller(matrix, mid)

        if smaller_numbers <= half:
            low = mid + 1
        else:
            high = mid - 1

    return low


def main():
    matrix = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
    r, c = 3, 3
    print(find_median(matrix, r, c))


if __name__ == '__main__':
    main()
