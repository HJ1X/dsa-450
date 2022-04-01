# python 3

from trees.tree_basics import Node


def lca(root, n1, n2):
    if root is None:
        return Node(-1)

    if root.data == n1 or root.data == n2:
        return root

    left = lca(root.left, n1, n2)
    right = lca(root.right, n1, n2)

    if left.data == -1 and right.data == -1:
        return left
    elif left.data == -1:
        return right
    elif right.data == -1:
        return left
    else:
        return root


def lca_parent(root, n1, n2):
    pass


def lca_bst(root, n1, n2):
    if root is None:
        return

    if root.data < n1 and root.data < n2:
        return lca_bst(root.right, n1, n2)

    elif root.data > n1 and root.data > n2:
        return lca_bst(root.left, n1, n2)

    else:
        return root


def main():
    pass


if __name__ == '__main__':
    main()
