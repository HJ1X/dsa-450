# python 3


def is_valid(left, right):
    matching_braces = ['()', '{}', '[]']

    pair = left + right
    if pair in matching_braces:
        return True
    else:
        return False


def check_parenthesis(x):
    opening_brackets = ['(', '[', '{']
    closing_brackets = [')', ']', '}']
    stack = []

    for brace in x:
        if brace in opening_brackets:
            stack.append(brace)

        elif brace in closing_brackets:
            if not stack:
                return False

            left = stack.pop()
            if not is_valid(left, brace):
                return False

    return not stack


def main():
    pass


if __name__ == '__main__':
    main()
