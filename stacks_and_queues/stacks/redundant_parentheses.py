# python 3

def find_redundant_parens(string):
    """
    The function assumes that the given string is a valid expression.

    :param string: String to validate without any whitespaces
    :return: Returns the index of first redundant parenthesis
    """

    stack = []
    for i in range(len(string)):
        if string[i] == ')':
            top = stack.pop()
            valid = False
            while string[top] != '(':
                if string[top] in ['+', '-', '/', '*']:
                    valid = True
                top = stack.pop()

            if not valid:
                return top
        else:
            stack.append(i)

    return -1


def main():
    string = input()
    print(find_redundant_parens(string))


if __name__ == '__main__':
    main()
