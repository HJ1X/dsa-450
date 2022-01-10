# python 3

# dp = [[False for i in range(1001)] for j in range(1001)]

def is_palindrome(string, i, j, dp):
    # base condition
    if i > j:
        return True

    # if already in DP
    # if dp[i][j]:
    #     return dp[i][j]

    # if end characters are not equal
    if string[i] != string[j]:
        dp[i][j] = False
        return dp[i][j]

    # calculate if not already present
    dp[i][j] = is_palindrome(string, i+1, j-1, dp)
    return dp[i][j]

    # while i <= j:
    #     if string[i] != string[j]:
    #         return False
    #     else:
    #         i += 1
    #         j -= 1
    #
    # return True


def count_palindrome(string):
    count = 0
    n = len(string)
    dp = [[False for i in range(n)] for j in range(n)]

    for i in range(len(string)):
        for j in range(i, len(string)):
            if is_palindrome(string,i,j, dp):
                count += 1
                # print(string[i:j+1])

    # for i in dp:
    #     print(i)
    return count


def is_pal(s, i, j, dp):
    if i > j:
        return True

    if dp[i][j]:
        return dp[i][j]

    if s[i] != s[j]:
        dp[i][j] = 0
        return dp[i][j]

    dp[i][j] = is_pal(s, i + 1, j - 1, dp)
    return dp[i][j]


def count_substrings(s):
    n = len(s)
    count = 0
    dp = [[False for i in range(n)] for j in range(n)]

    for i in range(n):
        for j in range(i + 1, n):
            if is_pal(s, i, j, dp):
                # print(s[i:j+1])
                count += 1
    return count


def count_pal_dp(string):
    n = len(string)
    count = 0
    dp = [[False for i in range(n)] for j in range(n)]

    for i in range(n):
        dp[i][i] = True
        count += 1

    for i in range(n-1):
        if string[i] == string[i+1]:
            dp[i][i+1] = True
            count += 1

    for gap in range(2, n):
        for i in range(n-gap):
            j = gap + i

            if string[i] == string[j]:
                dp[i][j] = dp[i+1][j-1]
                if dp[i+1][j-1]:
                    count += 1
                    print(string[i:j+1])
            else:
                dp[i][j] = False

    # for i in dp:
    #     print(i)
    return count


def main():
    string = input()
    # print(count_palindrome(string))
    # print(count_substrings(string))
    print(count_pal_dp(string))


if __name__ == '__main__':
    main()
