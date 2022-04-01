# python 3

def find_max_len(string):
    stack = [-1]
    max_len = 0

    for i in range(len(string)):
        if string[i] == '(':
            stack.append(i)

        else:
            stack.pop()
            if stack:
                curr_len = i - stack[-1]
                max_len = max(max_len, curr_len)
            else:
                stack.append(i)

    return max_len


def find_max_len_efficient(string):
    n = len(string)
    max_len = 0

    left_parens, right_parens = 0, 0
    for i in range(n):
        if string[i] == '(':
            left_parens += 1
        else:
            right_parens += 1

        if left_parens == right_parens:
            max_len = max(max_len, left_parens * 2)

        if right_parens > left_parens:    # If right parens are more string can't be valid
            left_parens, right_parens = 0, 0

    left_parens, right_parens = 0, 0
    for i in range(n-1, -1, -1):
        if string[i] == '(':
            left_parens += 1
        else:
            right_parens += 1

        if left_parens == right_parens:
            max_len = max(max_len, left_parens * 2)

        if left_parens > right_parens:    # If left parens are more string can't be valid
            left_parens, right_parens = 0, 0

    return max_len


def main():
    string = input()
    print(find_max_len(string))


if __name__ == '__main__':
    main()
