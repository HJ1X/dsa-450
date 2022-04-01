# python 3

def rotate_matrix(m, n, matrix):
    left, right = 0, n - 1
    top, bottom = 0, m - 1

    while left < right and top < bottom:
        top_left = matrix[top][left]

        for i in range(top, bottom):
            matrix[i][left] = matrix[i + 1][left]

        for i in range(left, right):
            matrix[bottom][i] = matrix[bottom][i + 1]

        for i in range(bottom, top, -1):
            matrix[i][right] = matrix[i - 1][right]

        for i in range(right, left, -1):
            matrix[top][i] = matrix[top][i - 1]

        matrix[top][left + 1] = top_left

        left += 1
        right -= 1
        top += 1
        bottom -= 1

    return matrix


def main():
    matrix = []
    while True:
        row = input()
        if not row:
            break

        row = list(map(int, row.split()))
        matrix.append(row)

    ans = rotate_matrix(len(matrix), len(matrix[0]), matrix)
    for row in ans:
        print(*row)


if __name__ == '__main__':
    main()
