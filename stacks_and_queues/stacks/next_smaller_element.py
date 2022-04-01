# python 3

def next_smaller_element(arr, n):
    ans = [-1] * n
    stack = [arr[n - 1]]

    for i in range(n - 2, -1, -1):
        while stack and stack[-1] >= arr[i]:
            stack.pop()

        if stack:
            ans[i] = stack[-1]

        stack.append(arr[i])

    return ans


def main():
    pass


if __name__ == '__main__':
    main()
