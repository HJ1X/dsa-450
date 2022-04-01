# python 3

def rotate_with_extra_matrix(matrix):
    num_rows, num_cols = len(matrix), len(matrix[0])
    new_matrix = [[None for i in range(num_cols)] for j in range(num_rows)]

    for row in range(num_rows):
        for col in range(num_cols):
            new_matrix[col][num_rows - row - 1] = matrix[row][col]

    return new_matrix


def rotate_in_place(matrix):
    num_rows, num_cols = len(matrix), len(matrix[0])

    for row in range(num_rows):
        for col in range(num_rows - row - 1):
            matrix[row][col], matrix[num_cols-col-1][num_rows-row-1] = \
                matrix[num_cols-col-1][num_rows-row-1], matrix[row][col]

    for row in range(num_rows//2):
        matrix[row], matrix[num_rows-row-1] = matrix[num_rows-row-1], matrix[row]

    return matrix


def rotate_in_place_transpose(matrix):
    num_rows, num_cols = len(matrix), len(matrix[0])

    for row in range(num_rows):
        for col in range(row):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for row in matrix:
        row.reverse()

    return matrix


def rotate_matrix_anticlockwise_transpose(matrix, n):
    num_rows, num_cols = len(matrix), len(matrix[0])

    for row in range(n):
        for col in range(row):
            matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

    for row in range(num_rows // 2):
        matrix[row], matrix[num_rows - row - 1] = matrix[num_rows - row - 1], matrix[row]

    return matrix


def rotate_in_place_corners(matrix):
    num_rows, num_cols = len(matrix), len(matrix[0])
    left, right = 0, num_cols - 1

    while left < right:
        for i in range(right - left):
            top, bottom = left, right
            top_left = matrix[top][left+i]

            # Swapping corners of squares
            matrix[top][left+i] = matrix[bottom-i][left]
            matrix[bottom-i][left] = matrix[bottom][right-i]
            matrix[bottom][right-i] = matrix[top+i][right]
            matrix[top+i][right] = top_left

        right -= 1
        left += 1

    return matrix


def main():
    matrix = []
    while True:
        row = input()
        if not row:
            break

        row = list(map(int, row.split()))
        matrix.append(row)

    ans = rotate_with_extra_matrix(matrix)
    for row in ans:
        print(*row)


if __name__ == '__main__':
    main()
