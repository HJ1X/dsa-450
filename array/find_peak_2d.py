# python 3

def find_max_in_column(matrix, col):
    max_index_in_col = 0
    for i in range(1, len(matrix)):
        if matrix[i][col] > matrix[max_index_in_col][col]:
            max_index_in_col = i

    return max_index_in_col


def find_2d_peak(matrix, l, r):
    # Find middle column
    mid = (l+r) // 2

    # Find maximum element in middle column
    max_in_mid_col = find_max_in_column(matrix, mid)

    # Check neighbours
    if 0 < mid < r and matrix[max_in_mid_col][mid - 1] > matrix[max_in_mid_col][mid]:
        return find_2d_peak(matrix, l, mid - 1)

    elif 0 < mid < r and matrix[max_in_mid_col][mid + 1] > matrix[max_in_mid_col][mid]:
        return find_2d_peak(matrix, mid + 1, r)

    else:
        return matrix[max_in_mid_col][mid]


def main():
    matrix = []
    while True:
        inp = input()
        if inp == '':
            break
        matrix.append(list(map(int, inp.split())))

    print(find_2d_peak(matrix, 0, len(matrix[0]) - 1))


if __name__ == '__main__':
    main()
