# python 3

def size(root):
    if root is None:
        return 0

    return 1 + size(root.left) + size(root.right)


def kth_largest(root, k):
    stack = []
    curr = root

    count = 0
    k = size(root) - k + 1

    while True:
        if curr:
            stack.append(curr)
            curr = curr.left

        elif stack:
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.data
            curr = curr.right

        else:
            break

    return -1


def kth_largest_reverse(root, k):
    stack = []
    curr = root
    count = 0

    while True:
        if curr:
            stack.append(curr)
            curr = curr.right

        elif stack:
            curr = stack.pop()
            count += 1
            if count == k:
                return curr.data
            curr = curr.left

        else:
            break

    return -1


def main():
    pass


if __name__ == '__main__':
    main()
