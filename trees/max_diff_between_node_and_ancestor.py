# python 3
from trees.tree_basics import BinaryTree


def find_min(root):
    if root is None:
        return float('inf')

    left = find_min(root.left)
    right = find_min(root.right)

    return min(left, right, root.data)


def find_max_difference(root):
    if root is None:
        return float('-inf')

    curr_diff = root.data - min(find_min(root.left), find_min(root.right))

    left_diff = find_max_difference(root.left)
    right_diff = find_max_difference(root.right)

    return max(curr_diff, left_diff, right_diff)


def find_max_diff_efficient_util(root, max_diff):
    if root is None:
        return float('inf')

    left = find_max_diff_efficient_util(root.left, max_diff)
    right = find_max_diff_efficient_util(root.right, max_diff)

    if root.data - min(left, right) > max_diff[0]:
        max_diff[0] = root.data - min(left, right)

    return min(left, right, root.data)


def find_max_diff_efficient(root):
    max_diff = [float('-inf')]
    find_max_diff_efficient_util(root, max_diff)

    return max_diff[0]


def find_max_diff_efficient_util_2(root, max_diff):
    if root is None:
        return float('inf'), max_diff

    left, max_diff_left = find_max_diff_efficient_util_2(root.left, max_diff)
    right, max_diff_right = find_max_diff_efficient_util_2(root.right, max_diff)

    min_value = min(left, right, root.data)
    max_diff = max(max_diff_left, max_diff_right, root.data - min(left, right))

    return min_value, max_diff


def find_max_diff_efficient_2(root):
    return find_max_diff_efficient_util_2(root, float('-inf'))[1]


def main():
    string = input()
    tree = BinaryTree.create_tree(string)
    print(find_max_diff_efficient_2(tree.root))


if __name__ == '__main__':
    main()
