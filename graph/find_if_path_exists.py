# python 3

from collections import deque


def is_valid(row, col, grid):
    rows = len(grid)
    cols = len(grid[0])

    return 0 <= row < rows and 0 <= col < cols


def visit_neighbors(row, col, grid, queue):
    row_offset = [0, -1, 0, 1]
    col_offset = [1, 0, -1, 0]

    for offset in range(4):
        curr_row = row + row_offset[offset]
        curr_col = col + col_offset[offset]

        if is_valid(curr_row, curr_col, grid) and grid[curr_row][curr_col] in [3, 2]:
            queue.appendleft((curr_row, curr_col))


def has_path(source_row, source_col, grid):
    queue = deque()
    queue.appendleft((source_row, source_col))

    while queue:
        row, col = queue.pop()

        if grid[row][col] == 2:
            return 1

        visit_neighbors(row, col, grid, queue)

    return 0


def is_possible(grid):
    rows = len(grid)
    cols = len(grid[0])

    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == 1:
                return has_path(row, col, grid)

    return 0


def main():
    matrix = []
    while True:
        row = input()
        if not row:
            break
        else:
            matrix.append(list(map(int, row.split())))

    print(is_possible(matrix))


if __name__ == '__main__':
    main()
