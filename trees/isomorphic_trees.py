# python 3

from trees.tree_basics import BinaryTree


def is_isomorphic(root1, root2):
    if root1 is None and root2 is None:
        return True

    if root1 is None or root2 is None:
        return False

    if root1.data != root2.data:
        return False

    return ((is_isomorphic(root1.left, root2.left) and
             is_isomorphic(root1.right, root2.right))
            or
            (is_isomorphic(root1.left, root2.right) and
             is_isomorphic(root1.right, root2.left)))


def main():
    string1 = input()
    tree1 = BinaryTree.create_tree(string1)
    string2 = input()
    tree2 = BinaryTree.create_tree(string2)
    print(is_isomorphic(tree1.root, tree2.root))


if __name__ == '__main__':
    main()
