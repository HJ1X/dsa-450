# python 3

def generate_ans(n, has_queen, ans):
    queens_row = []
    for col in range(n):
        for row in range(n):
            if has_queen[row][col]:
                queens_row.append(row + 1)

    ans.append(queens_row)


def is_safe(n, row, col, has_queen):
    # Upper diagonal
    curr_row = row
    curr_col = col
    while curr_row >= 0 and curr_col >= 0:
        if has_queen[curr_row][curr_col]:
            return False

        curr_row -= 1
        curr_col -= 1

    # Lower diagonal
    curr_row = row
    curr_col = col
    while curr_row < n and curr_col >= 0:
        if has_queen[curr_row][curr_col]:
            return False

        curr_row += 1
        curr_col -= 1

    # Left row
    curr_col = col
    while curr_col >= 0:
        if has_queen[row][curr_col]:
            return False

        curr_col -= 1

    return True


def find_config_util(n, col, has_queen, ans):
    if col == n:
        generate_ans(n, has_queen, ans)
        return

    for row in range(n):
        if is_safe(n, row, col, has_queen):
            has_queen[row][col] = True
            find_config_util(n, col + 1, has_queen, ans)
            has_queen[row][col] = False

    return


def find_config(n):
    ans = []
    has_queen = [[False for i in range(n)] for j in range(n)]  # chess board

    find_config_util(n, 0, has_queen, ans)


def find_config_efficient_util(n, col, left_row, upper_diagonal, lower_diagonal, curr_ans, ans):
    if col == n:
        ans.append(curr_ans.copy())
        return

    for row in range(n):
        if not left_row[row] and not lower_diagonal[row + col] and not upper_diagonal[n - 1 + col - row]:
            left_row[row] = True
            lower_diagonal[row + col] = True
            upper_diagonal[n - 1 + col - row] = True
            curr_ans.append(row + 1)

            find_config_efficient_util(n, col + 1, left_row, upper_diagonal, lower_diagonal, curr_ans, ans)

            left_row[row] = False
            lower_diagonal[row + col] = False
            upper_diagonal[n - 1 + col - row] = False
            curr_ans.pop()

    return


def find_config_efficient(n):
    ans = []
    curr_ans = []

    left_row = [False] * n
    upper_diagonal = [False] * (2 * n - 1)
    lower_diagonal = [False] * (2 * n - 1)

    find_config_efficient_util(n, 0, left_row, upper_diagonal, lower_diagonal, curr_ans, ans)
    return ans


def find_config_efficient_util_set(n, col, left_row, upper_diagonal, lower_diagonal, curr_ans, ans):
    if col == n:
        ans.append(curr_ans.copy())
        return

    for row in range(n):
        if row not in left_row and row + col not in lower_diagonal and row - col not in upper_diagonal:
            left_row.add(row)
            lower_diagonal.add(row + col)
            upper_diagonal.add(row - col)
            curr_ans.append(row + 1)

            find_config_efficient_util_set(n, col + 1, left_row, upper_diagonal, lower_diagonal, curr_ans, ans)

            left_row.remove(row)
            lower_diagonal.remove(row + col)
            upper_diagonal.remove(row - col)
            curr_ans.pop()

    return


def find_config_efficient_set(n):
    ans = []
    curr_ans = []

    left_row = set()
    upper_diagonal = set()
    lower_diagonal = set()

    find_config_efficient_util_set(n, 0, left_row, upper_diagonal, lower_diagonal, curr_ans, ans)
    return ans


def main():
    print(find_config_efficient_set(int(input())))


if __name__ == '__main__':
    main()
