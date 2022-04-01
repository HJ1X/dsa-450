# python 3

def find_ways_util(n, index):
    if index == n:
        return 1

    num_ways = 0
    num_ways += find_ways_util(n, index + 1)
    if index + 2 <= n:
        num_ways += find_ways_util(n, index + 2)

    return num_ways


def find_ways(n):
    return find_ways_util(n, 0)


def find_ways_2(n):
    if n <= 1:
        return n

    return find_ways_2(n-1) + find_ways_2(n-2)


def find_ways_util_dp(n, index, dp):
    if index == n:
        return 1

    if dp[index]:
        return dp[index]

    num_ways = 0
    num_ways += find_ways_util_dp(n, index + 1, dp)
    if index + 2 <= n:
        num_ways += find_ways_util_dp(n, index + 2, dp)

    dp[index] = num_ways
    return int(dp[index] % (1e9 + 7))


def find_ways_dp(n):
    dp = [None for i in range(n + 1)]
    return find_ways_util_dp(n, 0, dp)


def find_ways_tabulation(n):
    dp = [0 for i in range(n+1)]
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n+1):
        dp[i] = dp[i-1] + dp[i-2]

    return dp[n]


def find_ways_efficient(n):
    prev = 0
    curr = 1

    for i in range(n):
        prev, curr = curr, prev + curr

    return curr


def main():
    n = int(input())
    print(find_ways_efficient(n))


if __name__ == '__main__':
    main()
