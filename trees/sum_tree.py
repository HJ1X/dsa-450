# python 3

def create_sum_tree_util(root):
    if root is None:
        return 0

    tot_sum = 0
    tot_sum += root.data
    tot_sum += create_sum_tree_util(root.left)
    tot_sum += create_sum_tree_util(root.right)

    return tot_sum


def create_sum_tree_naive(root):
    if root is None:
        return

    root.data = create_sum_tree_util(root.left) + create_sum_tree_util(root.right)
    create_sum_tree_naive(root.left)
    create_sum_tree_naive(root.right)


def create_sum_tree_efficient(root):
    if root is None:
        return 0

    old_val = root.data
    left_sum = create_sum_tree_efficient(root.left)
    right_sum = create_sum_tree_efficient(root.right)

    root.data = left_sum + right_sum
    return old_val + root.data


def is_sum_tree_util(root):
    # If leaf node return its data
    if root.left is None and root.right is None:
        return root.data

    # If left node does not exist return 0 (root might have only right node)
    if root.left:
        left_tree = is_sum_tree_util(root.left)
        if left_tree == -1:
            return -1
    else:
        left_tree = 0

    # If right node does not exist return 0 (root might have only left node)
    if root.right:
        right_tree = is_sum_tree_util(root.right)
        if right_tree == -1:
            return -1
    else:
        right_tree = 0

    if root.data == left_tree + right_tree:
        return root.data + left_tree + right_tree
    else:
        return -1


def is_sum_tree(root):
    if is_sum_tree_util(root) == -1:
        return False
    else:
        return True


def main():
    pass


if __name__ == '__main__':
    main()
