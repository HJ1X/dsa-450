# python 3
from collections import deque
from sys import setrecursionlimit

setrecursionlimit(5000)


# ------ DFS Approach ------ #
def is_valid(row, col, matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if 0 <= row < num_rows and 0 <= col < num_cols and matrix[row][col] == 1:
        return True
    else:
        return False


def explore(matrix, row, col, visited):
    visited[row][col] = True

    row_deviations = [0, 1, 1, 1, 0, -1, -1, -1]  # clockwise, starting from right element
    col_deviations = [1, 1, 0, -1, -1, -1, 0, 1]

    for deviate in range(8):
        row_change = row + row_deviations[deviate]
        col_change = col + col_deviations[deviate]

        if is_valid(row_change, col_change, matrix) and not visited[row_change][col_change]:
            explore(matrix, row_change, col_change, visited)


def count_islands(matrix):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    visited = [[False for i in range(num_cols)] for j in range(num_rows)]
    count = 0

    for row in range(num_rows):
        for col in range(num_cols):
            if matrix[row][col] == 1 and not visited[row][col]:
                explore(matrix, row, col, visited)
                count += 1

    return count


# ------- BFS Approach ------ #
def is_inbound(row, col, grid):
    num_rows = len(grid)
    num_cols = len(grid[0])

    if 0 <= row < num_rows and 0 <= col < num_cols:
        return True
    else:
        return False


def bfs(row, col, grid, visited):
    row_offsets = [0, 1, 0, -1]
    col_offsets = [1, 0, -1, 0]

    queue = deque()
    queue.appendleft((row, col))

    while queue:
        curr_point = queue.pop()
        visited[curr_point[0]][curr_point[1]] = True

        for offset in range(4):
            curr_row = curr_point[0] + row_offsets[offset]
            curr_col = curr_point[1] + col_offsets[offset]

            if (is_inbound(curr_row, curr_col, grid) and
                grid[curr_row][curr_col] == '1' and
                not visited[curr_row][curr_col]
            ):
                queue.appendleft((curr_row, curr_col))
                visited

    return


def find_num_islands(grid):
    num_rows = len(grid)
    num_cols = len(grid[0])

    visited = [[False for i in range(num_cols)] for j in range(num_rows)]
    num_islands = 0

    for row in range(num_rows):
        for col in range(num_cols):
            if not visited[row][col] and grid[row][col] == '1':
                bfs(row, col, grid, visited)
                num_islands += 1

    return num_islands


def main():
    # matrix = []
    # while True:
    #     row = input()
    #     if not row:
    #         break
    #     else:
    #         matrix.append(list(map(int, row.split())))
    #
    # print(count_islands(matrix))
    print(find_num_islands(
        [["1", "1", "1", "1", "0"], ["1", "1", "0", "1", "0"], ["1", "1", "0", "0", "0"], ["0", "0", "0", "0", "0"]]))


if __name__ == '__main__':
    main()
