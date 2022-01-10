# python 3

def decode_ways_tabulation(string, dp):
    dp[len(string)] = 1
    dp[len(string) - 1] = 1
    for i in range(len(string) - 2, -1, -1):
        if string[i - 1] == '0':
            dp[i] = 0
        else:
            decode1 = dp[i + 1]
            decode2 = 0
            if i < len(string) and int(string[i-1 : i+1]) <= 26:
                decode2 = dp[i + 2]

            dp[i] = decode1 + decode2

    return dp[-1]


def decode_ways(string):
    # Some conditions missing - test case - 110
    # if len(string) == 1 or len(string) == 0:
    #     return 1
    #
    # decode1 = decode_ways(string[1:])
    # decode2 = 0
    # if int(string[:2]) <= 26:
    #     decode2 = decode_ways(string[2:])
    #
    # return decode1 + decode2

    if len(string) == 0:
        return 1

    if string[0] == '0':
        return 0

    decode1 = decode_ways(string[1:])
    decode2 = 0
    if len(string) > 1 and int(string[:2]) <= 26:
        decode2 = decode_ways(string[2:])

    return decode1 + decode2


def decode_ways_dp(string, dp):
    # complex conditions

    # if len(string) == 1 or len(string) == 0:
    #     return 1
    #
    # if dp[len(string)]:
    #     return dp[len(string)]
    #
    # decode1 = 0
    # if string[1] != '0':
    #     decode1 = decode_ways_dp(string[1:], dp)
    # decode2 = 0
    # if int(string[:2]) <= 26:
    #     if len(string) <= 2:
    #         decode2 = decode_ways_dp(string[2:], dp)
    #     elif string[2] != '0':
    #         decode2 = decode_ways_dp(string[2:], dp)
    #
    # dp[len(string)] = decode1 + decode2
    # return dp[len(string)]

    if len(string) == 0:
        return 1

    if string[0] == '0':
        return 0

    if dp[len(string)]:
        return dp[len(string)]

    decode1 = decode_ways_dp(string[1:], dp)
    decode2 = 0
    if len(string) > 1 and int(string[:2]) <= 26:
        decode2 = decode_ways_dp(string[2:], dp)

    dp[len(string)] = decode1 + decode2
    return dp[len(string)]


def main():
    string = input()
    dp = [None for i in range(len(string) + 1)]
    # print(decode_ways(string))
    # print(decode_ways_dp(string, dp))
    print(decode_ways_tabulation(string, dp))


if __name__ == '__main__':
    main()
