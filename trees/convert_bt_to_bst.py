# python 3
from trees.tree_basics import BinaryTree


def inorder(root, arr):
    if root is None:
        return

    inorder(root.left, arr)
    arr.append(root.data)
    inorder(root.right, arr)


def inorder_fill(root, arr):
    if root is None:
        return

    inorder_fill(root.left, arr)
    root.data = arr.pop()
    inorder_fill(root.right, arr)


def main():
    string = input()
    tree = BinaryTree.create_tree(string)

    arr = []
    inorder(tree.root, arr)
    arr.sort(reverse=True)

    print(inorder_fill(tree.root, arr))


if __name__ == '__main__':
    main()
