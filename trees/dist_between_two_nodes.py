# python 3

from trees.lca_of_two_nodes import lca as find_lca
from trees.tree_basics import BinaryTree


def find_dist(root, node):
    if root is None:
        return -1

    if root.data == node:
        return 0

    left_dist = find_dist(root.left, node)
    right_dist = find_dist(root.right, node)

    if left_dist > -1:
        return left_dist + 1
    elif right_dist > -1:
        return right_dist + 1
    else:
        return -1


def find_min_dist(root, a, b):
    lca = find_lca(root, a, b)
    return find_dist(lca, a) + find_dist(lca, b)


def main():
    string = input()
    tree = BinaryTree.create_tree(string)
    print(find_min_dist(tree.root, 4, 2))


if __name__ == '__main__':
    main()
