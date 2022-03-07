# python 3

def delete_middle(stack, k):
    if k == 1:
        stack.pop()
        return

    temp = stack.pop()
    delete_middle(stack, k-1)
    stack.append(temp)
    return


def main():
    stack = list(map(int, input().split()))
    mid = len(stack) // 2 + 1
    delete_middle(stack, mid)
    print(stack)


if __name__ == '__main__':
    main()
