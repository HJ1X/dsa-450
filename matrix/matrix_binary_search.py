# python 3
from typing import List


def search_matrix(matrix: List[List[int]], key: int) -> bool:
    # searching in column
    l, r = 0, len(matrix)
    while l < r:
        mid = (l + r) // 2
        if key < matrix[mid][0]:
            r = mid - 1

        else:
            l = mid

        if l == mid:
            break

    # searching in row
    l_row, r_row = 0, len(matrix[l]) - 1
    while l_row <= r_row:
        mid = (l_row + r_row) // 2
        if key == matrix[l][mid]:
            return True

        if key < matrix[l][mid]:
            r_row = mid - 1
        else:
            l_row = mid + 1

    return False


def main():
    matrix = [[1],[3],[5]]
    key = 5
    print(search_matrix(matrix, key))


if __name__ == '__main__':
    main()
