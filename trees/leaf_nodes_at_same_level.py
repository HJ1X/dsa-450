# python 3

def find_left_height(root):
    if root is None:
        return 0

    if root.left:
        next_node = root.left
    else:
        next_node = root.right

    return 1 + find_left_height(next_node)


def at_same_level(root, target_height, curr_height):
    if root is None:
        return True

    if root.left is None and root.right is None:
        if curr_height + 1 == target_height:
            return True
        else:
            return False

    if (at_same_level(root.left, target_height, curr_height + 1) and
            at_same_level(root.right, target_height, curr_height + 1)
    ):
        return True

    else:
        return False


def check(root):
    left_height = find_left_height(root)
    if at_same_level(root, left_height, 0):
        return True
    else:
        return False


def main():
    pass


if __name__ == '__main__':
    main()
