# python 3
from collections import deque


def fill_hashmap(root, hash_map, diagonal_value):
    if root is None:
        return

    if diagonal_value in hash_map:
        hash_map[diagonal_value].append(root.data)
    else:
        hash_map[diagonal_value] = [root.data]

    fill_hashmap(root.left, hash_map, diagonal_value + 1)
    fill_hashmap(root.right, hash_map, diagonal_value)

    return


def diagonal_hashmap(root):
    # param root: root of the given tree.
    # return: diagonal traversal of the given tree

    hash_map = {}
    fill_hashmap(root, hash_map, 0)
    ans = []

    for diagonal_value, nodes in hash_map.items():
        for node in nodes:
            ans.append(node)

    return ans


def diagonal_queue(root):
    ans = []
    queue = deque()

    node = root
    while node:
        ans.append(node.data)

        if node.left:
            queue.appendleft(node.left)

        if node.right:
            node = node.right
        else:
            if queue:
                node = node.pop()
            else:
                break

    return ans


def main():
    pass


if __name__ == '__main__':
    main()
