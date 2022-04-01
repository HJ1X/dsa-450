# python 3

def find_min_operations_util(arr, start, end):
    if start == end:
        return 0

    min_operations = float('inf')

    for partition in range(start, end):
        count = 0
        count += find_min_operations_util(arr, start, partition)
        count += find_min_operations_util(arr, partition + 1, end)
        count += arr[start - 1] * arr[partition] * arr[end]

        if count < min_operations:
            min_operations = count

    return min_operations


def find_min_operations(arr):
    n = len(arr)
    return find_min_operations_util(arr, 1, n - 1)


def find_min_operations_util_dp(arr, start, end, dp):
    if start == end:
        return 0

    if dp[start][end]:
        return dp[start][end]

    min_operations = float('inf')

    for partition in range(start, end):
        count = 0
        count += find_min_operations_util_dp(arr, start, partition, dp)
        count += find_min_operations_util_dp(arr, partition + 1, end, dp)
        count += arr[start - 1] * arr[partition] * arr[end]

        if count < min_operations:
            min_operations = count

    dp[start][end] = min_operations
    return dp[start][end]


def find_min_operations_dp(arr):
    n = len(arr)
    dp = [[None for i in range(n)] for j in range(n)]
    return find_min_operations_util_dp(arr, 1, n - 1, dp)


def find_min_operations_tabulation(arr):
    n = len(arr)
    dp = [[-1 for i in range(n)] for j in range(n)]

    for i in range(n):
        dp[i][0] = 0
        dp[0][i] = 0


def main():
    arr = list(map(int, input().split()))
    print(find_min_operations(arr))


if __name__ == '__main__':
    main()
