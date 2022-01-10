# python 3

def count_pairings(arr):
    if not arr:
        return 1

    current_friend = arr[0]
    remaining_friends = arr[1:]

    # if friend chooses to remain single
    count_when_alone = count_pairings(remaining_friends[:])

    # if friend pairs with every other friend
    count_when_paired = 0
    for i in range(len(remaining_friends)):
        # if ith friend is selected, remaining friends become
        new_rem_friends = remaining_friends[:i] + remaining_friends[i + 1:]
        count_when_paired += count_pairings(new_rem_friends)

    return count_when_alone + count_when_paired


def count_pairings_dp(arr, dp):
    if not arr:
        return 1

    if dp[len(arr)]:
        return dp[len(arr)]

    current_friend = arr[0]
    remaining_friends = arr[1:]

    # if friend chooses to remain single
    count_when_alone = count_pairings_dp(remaining_friends[:], dp)

    # if friend pairs with every other friend
    count_when_paired = 0
    for i in range(len(remaining_friends)):
        # if ith friend is selected, remaining friends become
        new_rem_friends = remaining_friends[:i] + remaining_friends[i + 1:]
        count_when_paired += count_pairings_dp(new_rem_friends, dp)

    dp[len(arr)] = count_when_alone + count_when_paired
    return dp[len(arr)]


def count_pairings_tabulation(arr, dp):
    n = len(arr)
    dp[1] = 1
    dp[2] = 2

    for i in range(3, n+1):
        # dp[i] will be:
        # 1. if i decides not to pair then, pairings will be equal to just dp[i-1] different pairs.
        # 2. if i decides to pair then, he will pair with every other element so, it will be equal to
        #     = number of remaining elements after choosing i * count of pairings possible with remaining i - 2 elements
        #     = (i-1) * dp[i-2]
        dp[i] = dp[i-1] + ((i-1) * dp[i-2])

    return dp[n]

def find_pairing(n):
    arr = [i+1 for i in range(n)]
    dp = [None for i in range(n+1)]

    # return count_pairings_dp(arr, dp)
    return count_pairings_tabulation(arr, dp)


def main():
    n = int(input())
    print(find_pairing(n))


if __name__ == '__main__':
    main()
