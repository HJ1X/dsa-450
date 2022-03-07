# python 3

def find_ceil(root, key):
    ceil = -1
    while root:
        if root.data == key:
            ceil = root.data
            return ceil

        elif root.data > key:
            ceil = root.data
            root = root.left

        else:
            root = root.right

    return ceil


def get_count_naive(root, low, high):
    curr = find_ceil(root, low)
    count = 0
    while curr <= high:
        if curr >= low:
            count += 1
        curr += 1
        curr = find_ceil(root, curr)

    return count


def get_count(root, low, high):
    if root is None:
        return 0

    if low <= root.data <= high:
        return 1 + get_count(root.left, low, high) + get_count(root.right, low, high)

    elif root.data > high:
        return get_count(root.left, low, high)

    else:
        return get_count(root.right, low, high)


def main():
    pass


if __name__ == '__main__':
    main()
