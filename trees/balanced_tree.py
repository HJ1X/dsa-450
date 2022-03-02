# python 3
from trees.basic_functions_on_tree import height
from trees.tree_basics import BinaryTree


def is_balanced(root):
    if root is None:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    if (
        abs(left_height - right_height) > 1 or
        not is_balanced(root.left) or
        not is_balanced(root.right)
    ):
        return False

    return True


def is_balanced_efficient_util(node):
    if node is None:
        return 0

    left_height = is_balanced(node.left)
    if left_height == -1:
        return -1

    right_height = is_balanced(node.right)
    if right_height == -1:
        return -1

    if abs(right_height - left_height) > 1:
        return -1

    return max(left_height, right_height) + 1


def is_balanced_efficient(root):
    if is_balanced_efficient_util(root) != -1:
        return True
    else:
        return False


def main():
    string = input()
    tree = BinaryTree.create_tree(string)
    print(is_balanced(tree.root))


if __name__ == '__main__':
    main()
