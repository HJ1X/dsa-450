# python 3

def find_ways_efficient(n, k):
    if n == 0:
        return 0

    if n == 1:
        return k

    same = k
    diff = k * (k-1)
    total = same + diff

    for i in range(3, n+1):
        same = diff
        diff = total * (k-1)
        total = same + diff

    return total


def find_ways_dp(n, k):
    if n == 0:
        return 0

    if n == 1:
        return k

    if n == 2:
        return k*k

    dp = [0 for i in range(n+1)]
    dp[1] = k
    dp[2] = k * k               # k * (k-1) (diff)  +  k (same)

    for i in range(3, n+1):
        same = dp[i-2] * (k-1)
        diff = dp[i-1] * (k-1)
        dp[i] = same + diff

    return dp[n]



def main():
    n = int(input())
    k = int(input())
    # print(find_ways_dp(n, k))
    print(find_ways_efficient(n, k))


if __name__ == '__main__':
    main()
