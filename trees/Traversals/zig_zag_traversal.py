# python 3

from collections import deque as deque_class


def zig_zag_traversal(root):
    if root is None:
        return

    zig_zag = []
    deque = deque_class()
    deque.appendleft(root)

    left_to_right = True

    while deque:
        n = len(deque)
        level = []

        for i in range(n):
            node = deque.pop()
            level.append(node.data)

            if node.left is not None:
                deque.appendleft(node.left)
            if node.right is not None:
                deque.appendleft(node.right)

        if left_to_right:
            zig_zag.extend(level)
        else:
            zig_zag.extend(reversed(level))

        # Reversing level order
        left_to_right = not left_to_right

    return zig_zag


def zig_zag_traversal_two_stacks(root):
    zig_zag = []

    curr_stack = []
    next_stack = []
    left_to_right = True

    curr_stack.append(root)

    while curr_stack:
        node = curr_stack.pop()
        zig_zag.append(node.data)

        if left_to_right:
            if node.left:
                next_stack.append(node.left)
            if node.right:
                next_stack.append(node.right)

        else:
            if node.right:
                next_stack.append(node.right)
            if node.left:
                next_stack.append(node.left)

        if not curr_stack:
            left_to_right = not left_to_right
            curr_stack, next_stack = next_stack, curr_stack

    return zig_zag


def main():
    pass


if __name__ == '__main__':
    main()
