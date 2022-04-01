# python 3

def find_maximum_path_tabulation(matrix, n):
    if n == 1:
        return matrix[0][0]

    max_path_sum = 0
    dp = [[0 for i in range(n)] for j in range(n)]

    for col in range(n):
        dp[0][col] = matrix[0][col]

    for row in range(1, n):
        for col in range(n):
            sum1 = dp[row-1][col-1] if col-1 >= 0 else 0
            sum2 = dp[row-1][col]
            sum3 = dp[row-1][col+1] if col+1 < n else 0

            dp[row][col] = matrix[row][col] + max(sum1, sum2, sum3)
            max_path_sum = max(max_path_sum, dp[row][col])

    return max_path_sum


def find_maximum_path_util_dp(matrix, row, col, n, dp):
    if row == n - 1:
        return matrix[row][col]

    if dp[row][col]:
        return dp[row][col]

    sum1 = find_maximum_path_util_dp(matrix, row + 1, col - 1, n, dp) if col - 1 >= 0 else 0
    sum2 = find_maximum_path_util_dp(matrix, row + 1, col, n, dp)
    sum3 = find_maximum_path_util_dp(matrix, row + 1, col + 1, n, dp) if col + 1 < n else 0

    dp[row][col] = matrix[row][col] + max(sum1, sum2, sum3)
    return dp[row][col]


def find_maximum_path_util(matrix, row, col, n, path_sum):
    if row == n:
        return path_sum

    curr_path_cost = matrix[row][col] + path_sum

    sum1 = find_maximum_path_util(matrix, row + 1, col - 1, n, curr_path_cost) if col - 1 >= 0 else 0
    sum2 = find_maximum_path_util(matrix, row + 1, col, n, curr_path_cost)
    sum3 = find_maximum_path_util(matrix, row + 1, col + 1, n, curr_path_cost) if col + 1 < n else 0

    return max(sum1, sum2, sum3)


def find_maximum_path(n, matrix):
    max_path_sum = 0
    dp = [[None for i in range(n)] for j in range(n)]

    for col in range(n):
        max_path_sum = max(find_maximum_path_util_dp(matrix, 0, col, n, dp), max_path_sum)

    return max_path_sum


def main():
    matrix = []
    while True:
        row = input()
        if not row:
            break
        else:
            matrix.append(list(map(int, row.split())))

    # print(find_maximum_path(len(matrix), matrix))
    print(find_maximum_path_tabulation(matrix, len(matrix)))


if __name__ == '__main__':
    main()
