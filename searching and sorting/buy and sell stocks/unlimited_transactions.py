# python 3

def find_max_profit(prices):
    max_profit = 0

    for i in range(len(prices) - 1):
        if prices[i] < prices[i+1]:
            max_profit += prices[i+1] - prices[i]

    return max_profit


def stock_buy_sell(prices, n):
    buy_index = 0
    made_profit = False
    max_profit = 0

    for i in range(n - 1):
        if prices[i + 1] < prices[i]:
            if buy_index != i:
                print('({} {})'.format(buy_index, i), end=' ')
                max_profit += prices[i] - prices[buy_index]
                made_profit = True
            buy_index = i + 1

    if buy_index < n - 1 and prices[n - 1] - prices[buy_index] > 0:
        print('({} {})'.format(buy_index, n - 1), end=' ')
        max_profit += prices[n-1] - prices[buy_index]
        made_profit = True

    if not made_profit:
        print('No Profit')

    print(max_profit)


def main():
    arr = list(map(int, input().split()))
    print(find_max_profit(arr))
    stock_buy_sell(arr, len(arr))


if __name__ == '__main__':
    main()
