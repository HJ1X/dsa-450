# python 3

from sys import setrecursionlimit
setrecursionlimit(5000)


def is_valid(row, col, matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if 0 <= row < num_rows and 0 <= col < num_cols and matrix[row][col] == 1:
        return True
    else:
        return False


def explore(matrix, row, col, visited):
    visited[row][col] = True

    row_deviations = [0, 1, 1, 1, 0, -1, -1, -1]     # clockwise, starting from right element
    col_deviations = [1, 1, 0, -1, -1, -1, 0, 1]

    for deviate in range(8):
        row_change = row + row_deviations[deviate]
        col_change = col + col_deviations[deviate]

        if is_valid(row_change, col_change, matrix) and not visited[row_change][col_change]:
            explore(matrix, row_change, col_change, visited)


def count_islands(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    visited = [[False for i in range(num_cols)] for j in range(num_rows)]
    count = 0

    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] == 1 and not visited[row][col]:
                explore(matrix, row, col, visited)
                count += 1

    return count


def main():
    matrix = []
    while True:
        row = input()
        if not row:
            break
        else:
            matrix.append(list(map(int, row.split())))

    print(count_islands(matrix))


if __name__ == '__main__':
    main()
