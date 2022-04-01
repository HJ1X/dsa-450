# python 3

from collections import deque
from trees.tree_basics import BinaryTree


def are_anagrams(arr1, arr2):
    if len(arr1) != len(arr2):
        return False

    arr1.sort()
    arr2.sort()

    for i in range(len(arr1)):
        if arr1[i] != arr2[i]:
            return False
    return True


def check_anagrams_levels(root1, root2):
    queue1 = deque([root1])
    queue2 = deque([root2])

    while queue1 and queue2:
        n1 = len(queue1)
        n2 = len(queue2)

        if n1 != n2:
            return False

        arr1 = []
        arr2 = []
        for i in range(n1):
            node1 = queue1.pop()
            node2 = queue2.pop()

            arr1.append(node1.data)
            arr2.append(node2.data)

            if node1.left:
                queue1.appendleft(node1.left)
            if node2.left:
                queue2.appendleft(node2.left)

            if node1.right:
                queue1.appendleft(node1.right)
            if node2.right:
                queue2.appendleft(node2.right)

        if not are_anagrams(arr1, arr2):
            return False

    return True


def main():
    string1 = input()
    string2 = input()
    tree1 = BinaryTree.create_tree(string1)
    tree2 = BinaryTree.create_tree(string2)

    print(check_anagrams_levels(tree1.root, tree2.root))


if __name__ == '__main__':
    main()
