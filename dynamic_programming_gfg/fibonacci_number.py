# Python 3

def fib_memoization(n, lookup):
    if n <= 1:
        return n

    if lookup[n-1] is None:
        lookup[n-1] = fib_memoization(n - 1, lookup)
    if lookup[n-2] is None:
        lookup[n-2] = fib_memoization(n - 2, lookup)
    return lookup[n-1] + lookup[n-2]


def fib_tabulation(n, lookup):
    lookup[0], lookup[1] = 0, 1
    for i in range(2, n + 1):
        lookup[i] = lookup[i-1] + lookup[i-2]
    return lookup[n]


def main():
    n = int(input())
    lookup = [None] * (n+1)
    # print(fib_memoization(n, lookup))
    print(fib_tabulation(n, lookup))


if __name__ == '__main__':
    main()
