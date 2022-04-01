# python 3

def spiral_traverse(matrix, r, c):
    answer = []
    start_row, end_row = 0, r
    start_col, end_col = 0, c

    while start_row < end_row and start_col < end_col:
        for i in range(start_col, end_col):
            answer.append(matrix[start_row][i])

        for i in range(start_row + 1, end_row):
            answer.append(matrix[i][end_col - 1])

        if end_row - start_row > 1:
            for i in range(end_col - 2, start_col - 1, - 1):
                answer.append(matrix[end_row - 1][i])

        if end_col - start_col > 1:
            for i in range(end_row - 2, start_row, -1):
                answer.append(matrix[i][start_col])

        start_row += 1
        end_row -= 1
        start_col += 1
        end_col -= 1

    return answer


def main():
    mat = [[6, 6, 2, 28, 2], [12, 26, 3, 28, 7], [22, 25, 3, 4, 23]]
    print(spiral_traverse(mat, 3, 5))


if __name__ == '__main__':
    main()
