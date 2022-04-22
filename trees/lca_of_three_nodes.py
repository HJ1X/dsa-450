# python 3

from trees.tree_basics import BinaryTree


def find_path(root, node, path):
    if root is None:
        return False

    path.append(root.data)

    if root.data == node:
        return True

    if find_path(root.left, node, path) or find_path(root.right, node, path):
        return True

    path.pop()
    return False


def find_lca(root, node1, node2, node3):
    path1, path2, path3 = [], [], []

    find_path(root, node1, path1)
    find_path(root, node2, path2)
    find_path(root, node3, path3)

    i = 0
    while i < len(path1) and i < len(path2) and i < len(path3):
        if path1[i] != path2[i] or path2[i] != path3[i]:
            break
        i += 1

    return path1[i - 1]


def main():
    string = input()
    tree = BinaryTree.create_tree(string)
    node1, node2, node3 = map(int, input().split())
    print(find_lca(tree.root, node1, node2, node3))


if __name__ == '__main__':
    main()
