# python 3

def find_next_greater_element(arr):
    stack = []
    ans = []

    for ele in reversed(arr):
        while stack and stack[-1] <= ele:
            stack.pop()

        if not stack:
            ans.append(-1)
        else:
            ans.append(stack[-1])

        stack.append(ele)

    return list(reversed(ans))


def main():
    pass


if __name__ == '__main__':
    main()
