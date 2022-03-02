# Python 3

from collections import deque
from trees.tree_basics import BinaryTree


def find_horizontal_distance(root):
    """ Returns max dist on left(min_dist) and right(max_dist) of root """

    def find_horizontal_distance_util(node, min_dist, max_dist, curr_dist):
        # ---------------- Pass by value code. Needs to return variable states ---------------- #
        if node is None:
            return min_dist, max_dist

        if curr_dist < min_dist:
            min_dist = curr_dist

        if curr_dist > max_dist:
            max_dist = curr_dist

        min_dist1, max_dist1 = find_horizontal_distance_util(node.left, min_dist, max_dist, curr_dist - 1)
        min_dist2, max_dist2 = find_horizontal_distance_util(node.right, min_dist, max_dist, curr_dist + 1)
        return min(min_dist1, max_dist2), max(max_dist1, max_dist2)

        # ------------------ Pass by reference code. No need to return values ---------------- #
        # if root is None:
        #     return min_dist, max_dist
        #
        # if curr_dist < min_dist[0]:
        #     min_dist[0] = curr_dist
        #
        # if curr_dist > max_dist[0]:
        #     max_dist[0] = curr_dist
        #
        # find_horizontal_distance_util(root.left, min_dist, max_dist, curr_dist - 1)
        # find_horizontal_distance_util(root.right, min_dist, max_dist, curr_dist + 1)
        # return

    return find_horizontal_distance_util(root, 0, 0, 0)

    # min_dist, max_dist = [0], [0]
    # find_horizontal_distance_util(root, min_dist, max_dist, 0)
    # return min_dist[0], max_dist[0]


def find_vertical_order_naive(root):
    # Find horizontal distance
    min_dist, max_dist = find_horizontal_distance(root)

    vertical_order = []

    def find_vertical_line(node, line_number, curr_dist):
        if node is None:
            return

        if line_number == curr_dist:
            vertical_order.append(node.data)

        find_vertical_line(node.left, line_number, curr_dist-1)
        find_vertical_line(node.right, line_number, curr_dist+1)
        return

    for line_number in range(min_dist, max_dist+1):
        find_vertical_line(root, line_number, 0)

    return vertical_order


def find_vertical_order_efficient(root):
    vertical_order = []
    hash_map = {}

    def store_dist_in_hash_map(node, curr_dist):
        if node is None:
            return

        # Doing inorder traversal
        store_dist_in_hash_map(node.left, curr_dist-1)
        if curr_dist in hash_map:
            hash_map[curr_dist].append(node.data)
        else:
            hash_map[curr_dist] = [node.data]
        store_dist_in_hash_map(node.right, curr_dist+1)
        return

    store_dist_in_hash_map(root, 0)

    for dist, nodes in hash_map.items():
        for value in nodes:
            vertical_order.append(value)

    return vertical_order


def find_vertical_order_efficient_and_ordered(root):
    vertical_order = []
    hash_map = {}

    max_dist, min_dist = 0, 0

    def store_dist_in_hash_map():
        nonlocal min_dist, max_dist
        queue = deque()
        queue.appendleft((root, 0))

        while queue:
            node, curr_dist = queue.pop()
            if min_dist > curr_dist:
                min_dist = curr_dist
            if max_dist < curr_dist:
                max_dist = curr_dist

            if curr_dist in hash_map:
                hash_map[curr_dist].append(node.data)
            else:
                hash_map[curr_dist] = [node.data]

            if node.left:
                queue.appendleft((node.left, curr_dist-1))
            if node.right:
                queue.appendleft((node.right, curr_dist+1))

        return

    store_dist_in_hash_map()

    for i in range(min_dist, max_dist+1):
        for value in hash_map[i]:
            vertical_order.append(value)

    return vertical_order


def main():
    string = input()
    tree = BinaryTree.create_tree(string)
    print(find_vertical_order_naive(tree.root))
    print(find_vertical_order_efficient(tree.root))
    print(find_vertical_order_efficient_and_ordered(tree.root))


if __name__ == '__main__':
    main()