# python 3

from collections import deque
from trees.tree_basics import BinaryTree


def find_ancestors(root, ancestor):
    queue = deque()
    queue.appendleft(root)

    while queue:
        node = queue.pop()

        if node.left:
            ancestor[node.left.data] = node.data
            queue.appendleft(node.left)

        if node.right:
            ancestor[node.right.data] = node.data
            queue.appendleft(node.right)

    return


def kth_ancestor(root, k, node):
    ancestor = {root.data: -1}
    find_ancestors(root, ancestor)

    for i in range(k):
        if ancestor[node] == -1:
            return -1
        node = ancestor[node]

    return node


def kth_ancestor_dfs(root, node, k, ancestor):
    if root is None:
        return False

    if (root.data == node or
        kth_ancestor_dfs(root.left, node, k, ancestor) or
        kth_ancestor_dfs(root.right, node, k, ancestor)
    ):
        if k[0] > 0:
            k[0] -= 1
            return True

        else:
            if ancestor[0] == -1:
                ancestor[0] = root.data

        return True


def main():
    string = input()
    tree = BinaryTree.create_tree(string)
    ancestor = [-1]
    k = [1]
    kth_ancestor_dfs(tree.root, 6, k, ancestor)
    print(ancestor[0])


if __name__ == '__main__':
    main()
