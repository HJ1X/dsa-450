# python 3

def find_max_profit(prices):
    max_profit = 0

    for i in range(len(prices) - 1):
        if prices[i] < prices[i+1]:
            max_profit += prices[i+1] - prices[i]

    return max_profit


def main():
    arr = [7,6,4,3,1]
    print(find_max_profit(arr))


if __name__ == '__main__':
    main()
