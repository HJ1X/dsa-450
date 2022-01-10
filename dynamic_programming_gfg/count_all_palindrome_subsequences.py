# python 3

def count_all_pal_subsequences(string):
    n = len(string)
    dp = [[0 for i in range(n)] for j in range(n)]

    for i in range(n):
        dp[i][i] = 1

    for i in range(n - 1):
        if string[i] == string[i + 1]:
            dp[i][i + 1] = 3
        else:
            dp[i][i + 1] = 2

    for gap in range(2, n):
        for i in range(n - gap):
            j = gap + i

            if string[i] == string[j]:
                dp[i][j] = dp[i][j - 1] + dp[i + 1][j] + 1
            else:
                dp[i][j] = dp[i][j - 1] + dp[i + 1][j] - dp[i + 1][j - 1]

    for i in dp:
        print(i)
    return dp[0][n - 1]


def main():
    arr = input()
    print(count_all_pal_subsequences(arr))


if __name__ == '__main__':
    main()
