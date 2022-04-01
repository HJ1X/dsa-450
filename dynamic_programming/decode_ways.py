# python 3

def count_ways_tabulation(string):
    dp = [0 for i in range(len(string) + 1)]

    dp[0] = 1
    dp[1] = 0 if string[0] == '0' else 1

    for i in range(2, len(string) + 1):
        # Checking for valid one digit numbers
        if string[i - 1] != '0':
            dp[i] += dp[i - 1]

        # Checking for valid two digits numbers
        if 10 <= int(string[i - 2:i]) <= 26:
            dp[i] += dp[i - 2]

    return dp[-1]


def count_ways(string):
    if len(string) == 0:
        return 1

    if string[0] == 0:
        return 0

    decode_ways = 0
    decode_ways += count_ways(string[1:])

    if len(string) > 1 and int(string[:2]) <= 26:
        decode_ways += count_ways(string[2:])

    return decode_ways


def count_ways_dp(string, dp):
    if len(string) == 0:
        return 1

    if string[0] == '0':
        return 0

    if dp[len(string)]:
        return dp[len(string)]

    decode_ways = 0
    decode_ways += count_ways_dp(string[1:], dp)

    if len(string) > 1 and int(string[:2]) <= 26:
        decode_ways += count_ways_dp(string[2:], dp)

    dp[len(string)] = decode_ways
    return dp[len(string)]


def count_ways_dp_2(string, index, dp):
    """ This approach is actually better from above because of use of hash_map for dp and
    to some extent, using index rather than string slicing"""
    if index in dp:
        return dp[index]

    if string[index] == '0':
        return 0

    decode_ways = 0
    decode_ways += count_ways_dp_2(string, index+1, dp)

    if index+1 < len(string) and 1 <= int(string[index:index+2]) <= 26:
        decode_ways += count_ways_dp_2(string, index+2, dp)

    dp[index] = decode_ways
    return dp[index]


def main():
    string = input()

    # dp = [None for i in range(len(string) + 1)]
    # print(count_ways_dp(string, dp))

    # dp = {len(string): 1}
    # print(count_ways_dp_2(string, 0, dp))

    print(count_ways_tabulation(string))


if __name__ == '__main__':
    main()
