# python 3

def find_max_profit(prices):
    n = len(prices)

    profit_till_i = [0] * n
    profit_from_i_to_n = [0] * n

    # calculating profit till i
    max_profit = 0
    min_price = float('inf')
    for i in range(n):
        curr_profit = prices[i] - min_price
        if curr_profit > max_profit:
            max_profit = curr_profit

        profit_till_i[i] = max_profit

        if prices[i] < min_price:
            min_price = prices[i]

    max_profit = 0
    max_price = float('-inf')
    for i in range(n - 1, -1, -1):
        curr_profit = max_price - prices[i]
        if curr_profit > max_profit:
            max_profit = curr_profit

        profit_from_i_to_n[i] = max_profit

        if prices[i] > max_price:
            max_price = prices[i]

    max_profit = 0
    for i in range(n):
        curr_profit = profit_till_i[i] + profit_from_i_to_n[i]
        if curr_profit > max_profit:
            max_profit = curr_profit

    return max_profit


def main():
    arr = [30, 40, 43, 50, 45, 20, 26, 40, 80, 50, 30, 15, 10, 25, 40, 45, 70, 50, 55]
    print(find_max_profit(arr))


if __name__ == '__main__':
    main()
