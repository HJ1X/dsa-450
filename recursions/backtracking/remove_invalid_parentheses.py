# python 3

def is_valid(string):
    stack = []
    for char in string:
        if char == '(':
            stack.append(char)

        elif char == ')':
            if not stack:
                return False

            top = stack.pop()
            if top != '(':
                return False

    return not stack


def find_valid_expression(string, parens_removed, min_parens_removed, ans, dp):
    if string in dp:
        return

    if is_valid(string):
        if parens_removed <= min_parens_removed[0]:
            if string not in ans:
                min_parens_removed[0] = parens_removed
                ans[string] = parens_removed
                return

    for i in range(len(string)):
        if string[i] in ['(', ')']:
            char = string[i]
            string = string[:i] + string[i + 1:]
            find_valid_expression(string, parens_removed + 1, min_parens_removed, ans, dp)
            string = string[:i] + char + string[i:]

    dp.add(string)
    return


def remove_invalid_parentheses(string):
    ans = {}
    min_parens_removed = [len(string) + 1]
    dp = set()

    find_valid_expression(string, 0, min_parens_removed, ans, dp)

    ans_list = []
    for string, parens_removed in ans.items():
        if parens_removed == min_parens_removed[0]:
            ans_list.append(string)

    return ans_list


def main():
    print(remove_invalid_parentheses(input()))


if __name__ == '__main__':
    main()
