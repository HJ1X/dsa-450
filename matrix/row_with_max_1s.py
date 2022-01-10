# python 3

# Row with maximum 1s | https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1#

# Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the first row that
# has the maximum number of 1's.

def row_with_max_1s(arr, n, m):
    # code here

    # r = 0
    # c = m - 1
    #
    # max_row = 0
    # while r < n and c >= 0:
    #     if arr[r][c - 1] == 1:
    #         c -= 1
    #
    #     else:
    #         r += 1
    #         if r < n and arr[r][c] == 1:
    #             max_row = r
    #
    # return max_row

    # or

    r = 0
    c = m - 1

    max_row = -1
    while r < n and c >= 0:
        if arr[r][c] == 1:
            c -= 1
            max_row = r

        else:
            r += 1

    return max_row


def main():
    matrix = [[0, 0],
              [0, 1],
              [0, 0],
              [0, 0],
              [0, 1],
              [0, 1]]
    n, m = 6, 2
    print(row_with_max_1s(matrix, n, m))


if __name__ == '__main__':
    main()
