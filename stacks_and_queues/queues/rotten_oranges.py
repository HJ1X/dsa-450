# python 3
from collections import deque


def rot_oranges(grid, i, j, queue):
    cols = len(grid[0])
    rows = len(grid)

    if i - 1 >= 0 and grid[i - 1][j] == 1:
        grid[i - 1][j] = 2
        queue.appendleft((i - 1, j))

    if i + 1 < rows and grid[i + 1][j] == 1:
        grid[i + 1][j] = 2
        queue.appendleft((i + 1, j))

    if j - 1 >= 0 and grid[i][j - 1] == 1:
        grid[i][j - 1] = 2
        queue.appendleft((i, j - 1))

    if j + 1 < cols and grid[i][j + 1] == 1:
        grid[i][j + 1] = 2
        queue.appendleft((i, j + 1))

    return


def find_time_to_rot_oranges(grid):
    queue = deque()
    total_oranges = 0

    # Initialize queue with all the rotten oranges and find fresh oranges
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] != 0:
                total_oranges += 1
            if grid[i][j] == 2:
                queue.appendleft((i, j))

    # Rot oranges until the queue is empty
    time = 0
    rotted_oranges = 0

    while queue:
        n = len(queue)
        rotted_oranges += n

        for i in range(n):
            i, j = queue.pop()
            rot_oranges(grid, i, j, queue)

        if not queue:
            break

        time += 1

    # Check if all oranges are rotten
    if rotted_oranges == total_oranges:
        return time
    else:
        return -1


def main():
    pass


if __name__ == '__main__':
    main()
