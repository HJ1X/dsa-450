# python 3

def insert_at_bottom(stack, data):
    if not stack:
        stack.append(data)
        return

    temp = stack.pop()
    insert_at_bottom(stack, data)
    stack.append(temp)


def reverse(stack):
    if not stack:
        return

    temp = stack.pop()
    reverse(stack)
    insert_at_bottom(stack, temp)
    return


def main():
    arr = list(map(int, input().split()))
    reverse(arr)
    print(arr)


if __name__ == '__main__':
    main()
