# python 3

def find_max_profit(prices, k):
    dp = [[0 for i in range(len(prices))] for j in range(k + 1)]

    for trans_num in range(1, k + 1):
        # keep track of max profit with a stock holding. Basically max of (max profit till (i-1) - share price at (
        # i-1)) i.e it would maximize profit keeping a holding of share (maximize trade values and calculating min
        # buy price after that), so that it could be used to calculate profit from selling at ith day

        # initially profit is minimum possible to consider negative values of profit as well
        max_profit_with_holding = float('-inf')

        for ith_day in range(1, len(prices)):
            max_profit = dp[trans_num][ith_day - 1]

            # optimization
            max_profit_with_holding = max(max_profit_with_holding, dp[trans_num - 1][ith_day - 1] - prices[ith_day - 1])
            max_profit = max(max_profit, max_profit_with_holding + prices[ith_day])

            # curr_day = 0
            # while curr_day < ith_day:
            #     profit = dp[trans_num - 1][curr_day] + (prices[ith_day] - prices[curr_day])
            #     if profit > max_profit:
            #         max_profit = profit
            #     curr_day += 1

            dp[trans_num][ith_day] = max_profit

    return dp[k][len(prices) - 1]


def stock_buy_sell(prices, n):
    buy_index = 0
    max_profit = []

    for i in range(n - 1):
        if prices[i + 1] < prices[i]:
            if buy_index != i:
                max_profit.append(prices[i] - prices[buy_index])
            buy_index = i + 1

    if buy_index < n - 1 and prices[n - 1] - prices[buy_index] > 0:
        max_profit.append(prices[n - 1] - prices[buy_index])

    print(max_profit)


def main():
    arr = [1, 2, 4, 2, 5, 7, 2, 4, 9, 0]
    k = 2
    print(find_max_profit(arr, k))
    print(stock_buy_sell(arr, len(arr)))


if __name__ == '__main__':
    main()
