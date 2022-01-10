# python 3

# You are given an array prices where prices[i] is the price of a given stock on the ith day. You want to maximize
# your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that
# stock. Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/ |  TC = O(N)


def find_max_profit(prices):
    curr_min = float('inf')
    max_profit = 0

    for price in prices:
        if price < curr_min:
            curr_min = price

        if price - curr_min > max_profit:
            max_profit = price - curr_min

    return max_profit


def main():
    arr = [7,6,4,3,1]
    print(find_max_profit(arr))


if __name__ == '__main__':
    main()
