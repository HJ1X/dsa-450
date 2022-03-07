# python 3
from trees.tree_basics import BinaryTree


def is_dead_end_util(root, min_limit, max_limit):
    if root is None:
        return True

    if max_limit - min_limit == 2:
        return False

    left = is_dead_end_util(root.left, min_limit, root.data)
    right = is_dead_end_util(root.right, root.data, max_limit)

    return left and right


def is_dead_end(root):
    return is_dead_end_util(root, 0, float('inf'))


def main():
    string = input()
    tree = BinaryTree.create_tree(string)
    print(is_dead_end(tree.root))

if __name__ == '__main__':
    main()
