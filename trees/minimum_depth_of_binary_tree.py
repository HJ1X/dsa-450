# python 3

from collections import deque
from trees.tree_basics import BinaryTree


def find_min_height_queue(root):
    queue = deque()
    queue.appendleft(root)
    level = 1

    while queue:
        n = len(queue)
        for i in range(n):
            node = queue.pop()
            if node.left is None and node.right is None:
                return level

            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)

        level += 1


def find_min_height_stack(root):
    stack = []
    curr = root

    min_height = float('inf')
    level = 1

    while True:
        if curr:
            stack.append((curr, level))
            curr = curr.left
            level += 1

        elif stack:
            curr, level = stack.pop()

            if not curr.right and not curr.left:
                min_height = min(min_height, level)

            if curr.right:
                level += 1
            curr = curr.right

        else:
            break

    return min_height


def find_min_height_recursive(root, level):
    if root is None:
        return float('inf')

    if root.left is None and root.right is None:
        return level

    level += 1
    left_height = find_min_height_recursive(root.left, level)
    right_height = find_min_height_recursive(root.right, level)

    return min(left_height, right_height)


def find_min_height_recursive_2(root):
    if root is None:
        return float('inf')

    if root.left is None and root.right is None:
        return 1

    left_height = find_min_height_recursive_2(root.left)
    right_height = find_min_height_recursive_2(root.right)

    return min(left_height, right_height) + 1


def main():
    string = input()
    tree = BinaryTree.create_tree(string)
    print(find_min_height_stack(tree.root))


if __name__ == '__main__':
    main()
