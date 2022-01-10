def check_smaller(element, matrix):
    count = 0
    for row in matrix:

        low = 0
        high = len(row) - 1

        while low <= high:
            mid = (low + high) // 2

            if row[mid] <= element:
                low = mid + 1
            else:
                high = mid - 1

        count += low

    return count


def median(matrix, r, c):
    # code here

    low = 0
    high = 1e9

    n_by_2 = (r * c) // 2

    while low <= high:
        mid = (high + low) // 2

        smaller_elements = check_smaller(mid, matrix)

        if smaller_elements <= n_by_2:
            low = mid + 1
        else:
            high = mid - 1

    return low


def main():
    matrix = [[1, 3, 5], [2, 6, 9], [3, 6, 9]]
    r, c = 3, 3
    print(median(matrix, r, c))


if __name__ == '__main__':
    main()
