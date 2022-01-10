# Python 3

# FInd out minimum number of coins to change the given amount with given coin denominations

def num_of_coins(amount, coins):
    if amount == 0:
        return 0
    min_coins = float('inf')
    for i in coins:
        if i <= amount:
            coins_i = num_of_coins(amount-i, coins) + 1
            min_coins = min(min_coins, coins_i)
    return min_coins


def main():
    coins = [1, 5, 6]
    amount = int(input())
    print(num_of_coins(amount, coins))


if __name__ == '__main__':
    main()
