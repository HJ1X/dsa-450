# python 3
from arrays.find_peak_1d import find_peak


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


def find_2d_peak_efficient_util(matrix, l, r):
    mid_row = (l + r) // 2
    # Find 1d peak function - TC = Log(n)
    peak = find_peak(matrix[mid_row], 0, len(matrix[0]) - 1)

    if mid_row > l and matrix[mid_row - 1][peak] > matrix[mid_row][peak]:
        return find_2d_peak_efficient_util(matrix, l, mid_row - 1)

    elif mid_row < r and matrix[mid_row + 1][peak] > matrix[mid_row][peak]:
        return find_2d_peak_efficient_util(matrix, mid_row + 1, r)

    else:
        return matrix[mid_row][peak]


def find_2d_peak_efficient(matrix):
    rows = len(matrix)
    return find_2d_peak_efficient_util(matrix, 0, rows - 1)


def main():
    matrix = []
    while True:
        inp = input()
        if inp == '':
            break
        matrix.append(list(map(int, inp.split())))

    # print(find_2d_peak(matrix, 0, len(matrix[0]) - 1))
    print(find_2d_peak_efficient(matrix))


if __name__ == '__main__':
    main()
