# python 3

def find_max_profit(prices):
    profits_till_day = [0] * len(prices)
    profits_after_day = [0] * len(prices)

    min_price = prices[0]
    max_profit = 0
    for i in range(1, len(prices)):
        curr_profit = prices[i] - min_price
        if curr_profit > max_profit:
            max_profit = curr_profit
            profits_till_day[i] = curr_profit
        else:
            profits_till_day[i] = max_profit

        if prices[i] < min_price:
            min_price = prices[i]

    max_price = prices[-1]
    max_profit = 0
    for i in range(len(prices) - 2, -1, -1):
        curr_profit = max_price - prices[i]
        if curr_profit > max_profit:
            max_profit = curr_profit
            profits_after_day[i] = curr_profit
        else:
            profits_after_day[i] = max_profit

        if prices[i] > max_price:
            max_price = prices[i]

    max_profit = 0
    for i in range(len(prices)):
        profit = profits_till_day[i] + profits_after_day[i]
        if profit > max_profit:
            max_profit = profit

    return max_profit


def main():
    arr = [30, 40, 43, 50, 45, 20, 26, 40, 80, 50, 30, 15, 10, 25, 40, 45, 70, 50, 55]
    print(find_max_profit(arr))


if __name__ == '__main__':
    main()
