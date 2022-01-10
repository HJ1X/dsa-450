# Python 3

# Implementing 0/1 knapsack problem for both with repetition and without repetition.


def knapsack_gold(dp, weight, items):
    for i in range(1, len(items) + 1):
        for w in range(1, weight + 1):
            dp[i][w] = dp[i-1][w]
            if items[i-1] <= w:
                w_i = items[i-1]
                val = dp[i-1][w-w_i] + w_i         # Adding w_i because weight is equal to value in given problem
                if val > dp[i][w]:
                    dp[i][w] = val

    return dp[len(items)][weight]


def knapsack_gold_memo(dp, weight, weight_items, val_items, i):
    if weight == 0 or i == 0:
        return 0

    if dp[i][weight] is not None:
        return dp[i][weight]

    val = knapsack_gold_memo(dp, weight, weight_items, val_items, i-1)
    dp[i][weight] = val

    val2 = 0
    if weight >= weight_items[i-1]:
        w_i = weight_items[i-1]
        val2 = knapsack_gold_memo(dp, weight - w_i, weight_items, val_items, i-1) + val_items[i-1]
        if val2 > val:
            dp[i][weight] = val2
            return val2

    return val


def main():
    weight = int(input())
    weight_items = list(map(int, input().split()))
    val_items = list(map(int, input().split()))

    # dp = [[0 for i in range(weight + 1)] for j in range(len(items) + 1)]
    dp = [[None for i in range(weight + 1)] for j in range(len(weight_items) + 1)]

    # print(knapsack_gold(dp, weight, items))
    print(knapsack_gold_memo(dp, weight, weight_items, val_items, len(weight_items)))


if __name__ == '__main__':
    main()
