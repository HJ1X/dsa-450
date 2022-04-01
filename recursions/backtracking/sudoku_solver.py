# python 3

def is_valid(grid, row, col, num):
    for curr_row in range(9):
        if grid[curr_row][col] == num:
            return False

    for curr_col in range(9):
        if grid[row][curr_col] == num:
            return False

    curr_row = 3 * (row // 3)
    curr_col = 3 * (col // 3)

    for i in range(curr_row, curr_row + 3):
        for j in range(curr_col, curr_col + 3):
            if grid[i][j] == num:
                return False

    return True


def solve_sudoku(grid):
    for row in range(9):
        for col in range(9):

            if grid[row][col] == 0:

                for num in range(1, 10):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num

                        if solve_sudoku(grid):
                            return True
                        else:
                            grid[row][col] = 0

                return False
    return True


def main():
    arr = list(map(int, input().split()))
    board = []

    for i in range(9):
        row = []
        for j in range(9):
            row.append(arr[9*i + j])
        board.append(row)

    solve_sudoku(board)
    print(board)


if __name__ == '__main__':
    main()
