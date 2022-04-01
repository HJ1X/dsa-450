# python 3

from collections import deque


def is_valid(matrix, row, col):
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    if (0 <= row < num_rows and 0 <= col < num_cols
            and matrix[row][col] == 1):
        return True
    return False


def find_shortest_dist_util(matrix, destination_row, destination_col, visited, queue):
    if not queue:
        return -1

    row, col, steps = queue.pop()

    if row == destination_row and col == destination_col:
        return steps

    row_deviations = [1, 0, 0, -1]
    col_deviations = [0, -1, 1, 0]

    for i in range(4):
        next_row = row + row_deviations[i]
        next_col = col + col_deviations[i]

        if is_valid(matrix, next_row, next_col) and not visited[next_row][next_col]:
            visited[next_row][next_col] = True
            queue.appendleft((next_row, next_col, steps + 1))

    return find_shortest_dist_util(matrix, destination_row, destination_col, visited, queue)


def find_shortest_dist(matrix, destination_row, destination_col):
    n = len(matrix)
    m = len(matrix[0])

    if matrix[0][0] == 0 or matrix[destination_row][destination_col] == 0:
        return -1

    visited = [[False for i in range(m)] for j in range(n)]
    queue = deque()
    queue.appendleft((0, 0, 0))

    return find_shortest_dist_util(matrix, destination_row, destination_col, visited, queue)


def find_shortest_dist_iterative(matrix, destination_row, destination_col):
    n = len(matrix)
    m = len(matrix[0])

    if matrix[0][0] == 0 or matrix[destination_row][destination_col] == 0:
        return -1

    queue = deque()
    queue.appendleft((0, 0, 0))

    visited = [[False for i in range(m)] for j in range(n)]
    visited[0][0] = True

    row_deviations = [1, 0, 0, -1]
    col_deviations = [0, -1, 1, 0]

    while queue:
        row, col, steps = queue.pop()

        if row == destination_row and col == destination_col:
            return steps

        for i in range(4):
            next_row = row + row_deviations[i]
            next_col = col + col_deviations[i]

            if is_valid(matrix, next_row, next_col) and not visited[next_row][next_col]:
                visited[next_row][next_col] = True    # not visited[row][col], it would create duplication
                queue.appendleft((next_row, next_col, steps + 1))

    return -1


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y


# A data structure for queue used in BFS
class queueNode:
    def __init__(self, pt: Point, dist: int):
        self.pt = pt  # The coordinates of the cell
        self.dist = dist  # Cell's distance from the source


# Check whether given cell(row,col)
# is a valid cell or not
def isValid(row: int, col: int, n, m):
    return (row >= 0) and (row < n) and (col >= 0) and (col < m)


# These arrays are used to get row and column
# numbers of 4 neighbours of a given cell


def shortestDistance(mat, destination_row, destination_col):
    n = len(mat)
    m = len(mat[0])

    if mat[0][0] != 1 or mat[destination_row][destination_col] != 1:
        return -1

    visited = [[False for i in range(m)] for j in range(n)]
    visited[0][0] = True

    q = deque()
    q.append((0, 0, 0))

    rowNum = [-1, 0, 0, 1]
    colNum = [0, -1, 1, 0]

    while q:
        curr = q.popleft()
        pt_x, pt_y, dist = curr

        if pt_x == destination_row and pt_y == destination_col:
            return dist

        for i in range(4):
            row = pt_x + rowNum[i]
            col = pt_y + colNum[i]

            if is_valid(mat, row, col) and not visited[row][col]:
                visited[row][col] = True
                q.append((row, col, dist+1))

    return -1


def main():
    matrix = []
    while True:
        row = input()
        if not row:
            break

        row = list(map(int, row.split()))
        matrix.append(row)

    destination_row, destination_col = map(int, input().split())

    ans = find_shortest_dist_iterative(matrix, destination_row, destination_col)
    # ans = shortestDistance(matrix, destination_row, destination_col)
    print(ans)


if __name__ == '__main__':
    main()
