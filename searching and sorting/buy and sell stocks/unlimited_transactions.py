# python 3

def find_max_profit(prices):
    max_profit = 0

    for i in range(len(prices) - 1):
        if prices[i] < prices[i+1]:
            max_profit += prices[i+1] - prices[i]

    return max_profit


def stock_buy_sell(prices, n):
    buy_index = 0
    ans = []

    for i in range(n - 1):
        if prices[i + 1] < prices[i]:
            if buy_index != i:
                ans.append((buy_index, i))
            buy_index = i + 1

    if buy_index < n - 1 and prices[n - 1] - prices[buy_index] > 0:
        ans.append((buy_index, n - 1))

    return ans


def stock_buy_sell_2(prices, n):
    max_profit = 0
    ans = []

    i = 0
    while i < n - 1:
        # Finding minimum value of stock to buy
        while i < n - 1 and prices[i + 1] <= prices[i]:
            i += 1
        buy_index = i

        if buy_index == n - 1:
            break

        # Finding maximum value of stock to sell
        while i < n - 1 and prices[i + 1] >= prices[i]:
            i += 1
        sell_index = i

        max_profit += prices[sell_index] - prices[buy_index]
        ans.append((buy_index, sell_index))

    return ans


def main():
    arr = list(map(int, input().split()))
    print(find_max_profit(arr))
    stock_buy_sell(arr, len(arr))


if __name__ == '__main__':
    main()
