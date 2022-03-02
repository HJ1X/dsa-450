# python 3

from collections import deque


def height(root):
    if root is None:
        return 0

    return 1 + max(height(root.left), height(root.right))


def diameter_naive(root):
    if not root:
        return 0

    diameter_left_tree = diameter_naive(root.left)
    diameter_right_tree = diameter_naive(root.right)
    diameter_root = 1 + height(root.left) + height(root.right)

    return max(
        diameter_left_tree,
        diameter_right_tree,
        diameter_root
    )


def height_diameter(root, diameter):
    if root is None:
        return 0

    left_height = height_diameter(root.left, diameter)
    right_height = height_diameter(root.right, diameter)

    diameter[0] = max(diameter[0],
                      1 + left_height
                      + right_height)
    return 1 + max(left_height, right_height)


def mirror_tree(root):
    if root is None:
        return

    root.left, root.right = root.right, root.left

    mirror_tree(root.left)
    mirror_tree(root.right)
    return


def diameter_efficient(self, root):
    diameter = [float('-inf')]
    height_diameter(root, diameter)
    return diameter[0]


def left_view(root):
    ans = []

    queue = deque()
    queue.appendleft(root)

    while queue:
        n = len(queue)
        for i in range(n):
            node = queue.pop()

            if i == 0:
                ans.append(node.data)

            if node.left:
                queue.appendleft(node.left)
            if node.right:
                queue.appendleft(node.right)

    return ans


def top_view(root):
    if root is None:
        return

    ans = deque()
    ans.appendleft(root.data)

    min_dist, max_dist = 0, 0

    queue = deque()
    queue.appendleft((root, 0))

    while queue:
        node, curr_dist = queue.pop()

        # Whenever new extreme is encounter add to top view
        if min_dist > curr_dist:
            ans.appendleft(node.data)
            min_dist = curr_dist

        if max_dist < curr_dist:
            ans.append(node.data)
            max_dist = curr_dist

        if node.left:
            queue.appendleft((node.left, curr_dist - 1))
        if node.right:
            queue.appendleft((node.right, curr_dist + 1))

    return ans


def bottom_view(root):
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

            hash_map[curr_dist] = node.data

            if node.left:
                queue.appendleft((node.left, curr_dist - 1))
            if node.right:
                queue.appendleft((node.right, curr_dist + 1))

        return

    store_dist_in_hash_map()

    for i in range(min_dist, max_dist + 1):
        vertical_order.append(hash_map[i])

    return vertical_order


def main():
    pass


if __name__ == '__main__':
    main()

