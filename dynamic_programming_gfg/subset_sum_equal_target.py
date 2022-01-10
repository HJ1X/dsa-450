# Python 3

def find_subsets(arr, target, dp, subsets, temp):
    if target == 0:
        subsets.append(temp)
        return

    elements = len(arr)
    if dp[elements][target]:
        # Find if subset can be formed when element is not included
        if dp[elements - 1][target]:
            find_subsets(arr[:elements-1], target, dp, subsets, temp[:])

        # Find if subset can be formed when element is included
        if arr[elements - 1] <= target and dp[elements - 1][target - arr[elements - 1]]:
            find_subsets(arr[:elements-1], target - arr[elements - 1], dp, subsets, temp + [arr[elements - 1]])


def subset_sum(arr, target):
    dp = [[False for j in range(target + 1)] for i in range(len(arr) + 1)]

    for i in range(len(arr) + 1):
        for j in range(target + 1):
            if j == 0:
                dp[i][j] = True
            elif i == 0:
                dp[i][j] = False
            else:
                dp[i][j] = dp[i-1][j]
                if arr[i-1] <= j:
                    x = j - arr[i-1]
                    val = dp[i-1][x]
                    if val is True:
                        dp[i][j] = True

    # printing all subsets
    subsets = []
    temp = []
    find_subsets(arr, target, dp, subsets, temp)
    print(subsets)

    return dp[len(arr)][target]


def main():
    arr = list(map(int, input().split()))
    target = int(input())
    print(subset_sum(arr, target))


if __name__ == '__main__':
    main()
