# python 3

def is_palindrome(string, start, end):
    while start < end:
        if string[start] != string[end]:
            return False

        start += 1
        end -= 1

    return True


def find_min_cuts_util(string, start, end):
    if is_palindrome(string, start, end):
        return 0

    min_cuts = float('inf')

    for partition in range(start, end):
        cuts = 1
        cuts += find_min_cuts_util(string, start, partition)
        cuts += find_min_cuts_util(string, partition + 1, end)

        if cuts < min_cuts:
            min_cuts = cuts

    return min_cuts


def find_min_cuts(string):
    start = 0
    end = len(string) - 1

    return find_min_cuts_util(string, start, end)


def find_min_cuts_util_dp(string, start, end, dp):
    if dp[start][end]:
        return dp[start][end]

    if is_palindrome(string, start, end):
        return 0

    min_cuts = float('inf')

    for partition in range(start, end):
        cuts = 1
        cuts += find_min_cuts_util_dp(string, start, partition, dp)
        cuts += find_min_cuts_util_dp(string, partition + 1, end, dp)

        if cuts < min_cuts:
            min_cuts = cuts

    dp[start][end] = min_cuts
    return dp[start][end]


def find_min_cuts_dp(string):
    n = len(string)

    start = 0
    end = n - 1

    dp = [[None for i in range(n)] for j in range(n)]

    return find_min_cuts_util_dp(string, start, end, dp)


def main():
    string = input()
    print(find_min_cuts_dp(string))


if __name__ == '__main__':
    main()
