# python 3

from collections import defaultdict as ddict


def is_valid(grid):
    # Check validity of rows
    for row in range(9):
        hash_set = set()
        for col in range(9):
            if grid[row][col] == 0:
                continue

            if grid[row][col] in hash_set:
                return 0

            hash_set.add(grid[row][col])

    # Check validity of columns
    for col in range(9):
        hash_set = set()
        for row in range(9):
            if grid[row][col] == 0:
                continue

            if grid[row][col] in hash_set:
                return 0

            hash_set.add(grid[row][col])

    # Check validity of internal 3 X 3 grids
    for grid_row in range(3):
        for grid_col in range(3):
            hash_set = set()
            for row in range(3):
                for col in range(3):
                    row_val = (grid_row * 3) + row
                    col_val = (grid_col * 3) + col

                    if grid[row_val][col_val] == 0:
                        continue

                    if grid[row_val][col_val] in hash_set:
                        return 0

                    hash_set.add(grid[row_val][col_val])

    return 1


def is_valid_efficient(grid):
    row_hash_map = ddict(set)
    col_hash_map = ddict(set)
    grid_hash_map = ddict(set)

    for row in range(9):
        for col in range(9):
            ele = grid[row][col]

            if ele == 0:
                continue

            if (ele in row_hash_map[row] or
                ele in col_hash_map[col] or
                ele in grid_hash_map[(row // 3, col // 3)]):
                return 0

            row_hash_map[row].add(ele)
            col_hash_map[col].add(ele)
            grid_hash_map[(row // 3, col // 3)].add(ele)

    return 1


def main():
    pass


if __name__ == '__main__':
    main()
