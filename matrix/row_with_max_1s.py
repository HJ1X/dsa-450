# python 3

# Row with maximum 1s | https://practice.geeksforgeeks.org/problems/row-with-max-1s0023/1#

# Given a boolean 2D array of n x m dimensions where each row is sorted. Find the 0-based index of the first row that
# has the maximum number of 1's.

def row_with_max_1s(arr, n, m):
    row = 0
    col = m - 1

    ans = -1
    while row < n and col >= 0:
        if arr[row][col] == 0:
            row += 1

        else:
            ans = row
            col -= 1

    return ans


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
