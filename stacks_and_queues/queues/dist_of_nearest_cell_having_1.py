# python 3

from collections import deque


def find_dist(grid, i, j, queue, ans, rows, cols, dist):
    if i - 1 >= 0 and grid[i - 1][j] == 0 and ans[i - 1][j] is None:
        ans[i - 1][j] = dist
        queue.appendleft((i - 1, j))

    if i + 1 < rows and grid[i + 1][j] == 0 and ans[i + 1][j] is None:
        ans[i + 1][j] = dist
        queue.appendleft((i + 1, j))

    if j - 1 >= 0 and grid[i][j - 1] == 0 and ans[i][j - 1] is None:
        ans[i][j - 1] = dist
        queue.appendleft((i, j - 1))

    if j + 1 < cols and grid[i][j + 1] == 0 and ans[i][j + 1] is None:
        ans[i][j + 1] = dist
        queue.appendleft((i, j + 1))

    return


def find_nearest(grid):
    n, m = len(grid), len(grid[0])
    queue = deque()
    ans = [[None for i in range(m)] for j in range(n)]

    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == 1:
                queue.appendleft((i, j))
                ans[i][j] = 0

    dist = 1
    while queue:
        num = len(queue)

        for _ in range(num):
            i, j = queue.pop()
            find_dist(grid, i, j, queue, ans, n, m, dist)

        if not queue:
            break

        dist += 1

    return ans


def main():
    grid = [[0, 1, 1, 0],
            [1, 1, 0, 0],
            [0, 0, 1, 1]]

    print(find_nearest(grid))



if __name__ == '__main__':
    main()
