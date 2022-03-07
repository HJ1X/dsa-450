# python 3
from trees.tree_basics import Node


def create_tree(arr):
    if not arr:
        return

    mid = len(arr) // 2
    root = Node(arr[mid])
    root.left = create_tree(arr[:mid])
    root.right = create_tree(arr[mid + 1:])
    return root


def preorder(root, arr):
    if root is None:
        return

    arr.append(root.data)
    preorder(root.left, arr)
    preorder(root.right, arr)

    return arr


def main():
    pass


if __name__ == '__main__':
    main()
