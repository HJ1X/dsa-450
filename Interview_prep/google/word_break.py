# python 3

res = []


def word_break(string, ans, dictionary):
    global res

    if string == '':
        res.append(ans)
        return

    for i in range(len(string)):
        if string[0:i + 1] in dictionary:
            left = string[:i+1]
            word_break(string[i+1:], ans + ' ' + left, dictionary)

    return res


def word_break_dp(string, dictionary, dp):
    # Incorrect
    if string == '':
        return True

    if string in dp:
        if dp[string]:
            return True

    for i in range(len(string)):
        left = string[:i+1]
        if left in dictionary:
            is_valid = word_break_dp(string[i+1:], dictionary, dp)
            dp[string[i+1:]] = is_valid
            if is_valid:
                return True

    dp[string] = False
    return False


def word_break_tabulation(string, dictionary, dp):
    for i in range(1, len(string) + 1):
        for j in range(i):
            right = string[j:i]
            if dp[j] and right in dictionary:
                dp[i] = True
                break
    return dp[len(string)]


def main():
    dictionary = {"i", "love", 'sam', 'samsung', 'sung'}
    string = 'ilovesamsung'
    dp = [False for i in range(len(string) + 1)]
    dp[0] = True
    print(word_break_tabulation(string, dictionary, dp))
    # print(word_break_dp(string, dictionary, dp))
    # print(word_break(string, '', dictionary))


if __name__ == '__main__':
    main()
