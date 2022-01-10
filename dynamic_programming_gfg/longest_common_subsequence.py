# python 3

def lcs_tab_print(str1, str2):
    dp = [[[0, ''] for i in range(len(str2) + 1)] for j in range(len(str1) + 1)]

    for i in range(1, len(str1) + 1):
        for j in range(1, len(str2) + 1):
            if str1[i - 1] == str2[j - 1]:
                dp[i][j][0] = 1 + dp[i - 1][j - 1][0]
                dp[i][j][1] += dp[i-1][j-1][1] + str1[i-1]

            else:
                x = dp[i - 1][j][0]
                x_str = dp[i - 1][j][1]
                y = dp[i][j - 1][0]
                y_str = dp[i][j - 1][1]

                if x > y:
                    dp[i][j][0], dp[i][j][1] = x, x_str
                else:
                    dp[i][j][0], dp[i][j][1] = y, y_str

    return dp[len(str1)][len(str2)][0], dp[len(str1)][len(str2)][1]


def lcs_memo_print(res, dp, str1, str2, i, j):
    if i == len(str1) or j == len(str2):
        return res, 0

    # If elements are same in two strings just add 1 to count and find lcs by removing those elements from both
    # strings, i.e. i-1 and i-2
    if str1[i] == str2[j]:
        res += str1[i]
        if dp[i + 1][j + 1] is None:
            res, dp[i + 1][j + 1] = lcs_memo_print(res, dp, str1, str2, i + 1, j + 1)
        print(res)
        return res, dp[i + 1][j + 1] + 1

    # If elements are not equal then, just find max of both strings removing one element from 1 string at a
    # time, i.e. max(lcs(i-1, j), lcs(i, j-1))
    else:
        if dp[i][j + 1] is None:
            res, dp[i][j + 1] = lcs_memo_print(res, dp, str1, str2, i, j + 1)
        if dp[i + 1][j] is None:
            res, dp[i + 1][j] = lcs_memo_print(res, dp, str1, str2, i + 1, j)
        return res, max(dp[i][j + 1], dp[i + 1][j])


def lcs_memoization(dp, str1, str2, i, j):
    if i == len(str1) or j == len(str2):
        return 0

    # If elements are same in two strings just add 1 to count and find lcs by removing those elements from both
    # strings, i.e. i-1 and i-2
    if str1[i] == str2[j]:
        if dp[i + 1][j + 1] is None:
            dp[i + 1][j + 1] = lcs_memoization(dp, str1, str2, i + 1, j + 1)
        return dp[i + 1][j + 1] + 1

    # If elements are not equal then, just find max of both strings removing one element from 1 string at a
    # time, i.e. max(lcs(i-1, j), lcs(i, j-1))
    else:
        if dp[i][j + 1] is None:
            dp[i][j + 1] = lcs_memoization(dp, str1, str2, i, j + 1)
        if dp[i + 1][j] is None:
            dp[i + 1][j] = lcs_memoization(dp, str1, str2, i + 1, j)
        return max(dp[i][j + 1], dp[i + 1][j])


def lcs(str1, str2, i, j):
    if i == len(str1) or j == len(str2):
        return 0

    if str1[i] == str2[j]:
        return 1 + lcs(str1, str2, i + 1, j + 1)
    else:
        return max(lcs(str1, str2, i, j + 1), lcs(str1, str2, i + 1, j))


def main():
    str1 = input()
    str2 = input()

    dp = [[None for i in range(len(str2)+1)] for j in range(len(str1)+1)]
    # print(lcs(str1, str2, 0, 0))
    # print(lcs_memoization(dp, str1, str2, 0, 0))
    res = ''
    print(res)
    # print(lcs_memo_print(res, dp, str1, str2, 0, 0))
    print(lcs_tab_print(str1, str2))


if __name__ == '__main__':
    main()
