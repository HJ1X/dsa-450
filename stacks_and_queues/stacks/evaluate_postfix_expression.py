# python 3

def do_operation(char, a, b):
    if char == '+':
        ans = a + b

    elif char == '-':
        ans = a - b

    elif char == '*':
        ans = a * b

    else:
        ans = a // b

    return ans


def evaluate_postfix(string):
    stack = []
    for char in string:
        if char.isdigit():
            stack.append(int(char))

        else:
            b = stack.pop()
            a = stack.pop()

            ans = do_operation(char, a, b)
            stack.append(ans)

    return stack[-1]


def main():
    pass


if __name__ == '__main__':
    main()
