# python 3

def insert_at_correct_place(stack, data):
    if not stack or stack[-1] < data:
        stack.append(data)
        return

    temp = stack.pop()
    insert_at_correct_place(stack, data)
    stack.append(temp)
    return


def sort_stack(stack):
    if not stack:
        return

    temp = stack.pop()
    sort_stack(stack)
    insert_at_correct_place(stack, temp)
    return


def main():
    pass


if __name__ == '__main__':
    main()
