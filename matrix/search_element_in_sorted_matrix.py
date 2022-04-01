# python 3

from typing import List


def search_matrix_linear(self, matrix: List[List[int]], key: int) -> bool:
    r = 0
    c = len(matrix[0]) - 1

    while r < len(matrix) and c >= 0:
        if matrix[r][c] == key:
            return True

        if matrix[r][c] < key:
            r += 1
        else:
            c -= 1

    return False


def find_in_row(matrix, row, target):
    low = 0
    high = len(matrix[row]) - 1

    while low <= high:
        mid = (low + high) // 2

        if matrix[row][mid] == target:
            return True

        elif matrix[row][mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return False


def search_matrix(matrix: List[List[int]], target: int) -> bool:
    low = 0
    high = len(matrix) - 1

    while low <= high:
        mid = (low + high) // 2

        if target < matrix[mid][0]:
            high = mid - 1
        elif target > matrix[mid][-1]:
            low = mid + 1
        else:
            return find_in_row(matrix, mid, target)


def main():
    matrix = [[1],[3],[5]]
    key = 5
    print(search_matrix(matrix, key))


if __name__ == '__main__':
    main()
