# python 3

def is_valid(row, col, matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if (0 <= row < num_rows and 0 <= col < num_cols
            and matrix[row][col] == 1):
        return True
    return False


def find_path_util(matrix, row, col, path, res, visited):
    if row == len(matrix) - 1 and col == len(matrix[0]) - 1:
        res.append(''.join(path))
        return

    directions = 'DLRU'  # Lexicographical order
    row_deviations = [1, 0, 0, -1]
    col_deviations = [0, -1, 1, 0]

    for i in range(4):
        next_row = row_deviations[i] + row
        next_col = col_deviations[i] + col

        if (
            is_valid(next_row, next_col, matrix)
            and not visited[next_row][next_col]
        ):
            visited[row][col] = True
            path.append(directions[i])
            find_path_util(matrix, next_row, next_col, path, res, visited)
            path.pop()
            visited[row][col] = False

    return


def find_path(matrix, n):
    if matrix[0][0] == 0:
        return []

    path = []
    res = []
    visited = [[False
                for i in range(len(matrix[0]))]
               for j in range(len(matrix))]

    find_path_util(matrix, 0, 0, path, res, visited)
    return res


def main():
    matrix = []
    while True:
        row = input()
        if not row:
            break

        row = list(map(int, row.split()))
        matrix.append(row)

    ans = find_path(matrix, len(matrix))
    print(ans)


if __name__ == '__main__':
    main()
