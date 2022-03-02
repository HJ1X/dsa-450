# python 3

from collections import deque as deque_class
from trees.tree_basics import BinaryTree


def level_order(root):
    if root is None:
        return

    bfs = []
    deque = deque_class()
    deque.appendleft(root)

    while deque:
        node = deque.pop()
        bfs.append(node.data)
        if node.left is not None:
            deque.appendleft(node.left)
        if node.right is not None:
            deque.appendleft(node.right)

    return bfs


def reverse_level_order(root):
    if root is None:
        return

    stack = []
    deque = deque_class()
    deque.appendleft(root)

    while deque:
        node = deque.pop()
        stack.append(node.data)
        if node.right is not None:
            deque.appendleft(node.right)
        if node.left is not None:
            deque.appendleft(node.left)

    return reversed(stack)


def inorder_recursive(root):
    if root is None:
        return

    inorder_recursive(root.left)
    # <---------- process node here --------> #
    inorder_recursive(root.right)

    return


def inorder_iterative(root):
    stack = []
    curr = root

    while True:
        if curr is not None:
            stack.append(curr)
            curr = curr.left

        elif stack:
            curr = stack.pop()
            # <---------- process node here --------> #
            curr = curr.right

        else:
            break

    return


def preorder_recursive(root):
    if root is None:
        return

    # <---------- process node here --------> #
    preorder_recursive(root.left)
    preorder_recursive(root.right)

    return


def preorder_iterative(root):
    stack = []
    curr = root

    while True:
        if curr is not None:
            # <---------- process node here --------> #
            stack.append(curr)
            curr = curr.left

        elif stack:
            curr = stack.pop()
            curr = curr.right

        else:
            break

    return


def postorder_recursive(root, arr):
    if root is None:
        return

    postorder_recursive(root.left, arr)
    postorder_recursive(root.right, arr)
    # <---------- process node here --------> #

    return


def postorder_iterative_2_stacks(root):
    stack1 = [root]
    stack2 = []

    while stack1:
        ele = stack1.pop()

        if ele.left is not None:
            stack1.append(ele.left)
        if ele.right is not None:
            stack1.append(ele.right)

        stack2.append(ele)

    for node in reversed(stack2):
        # <---------- process node here --------> #
        pass

    return


def top(stack):
    return stack[-1]


def postorder_iterative_1_stack(root):
    stack = []
    curr = root

    while True:
        if curr is not None:
            stack.append(curr)
            curr = curr.left

        elif stack:
            temp = top(stack)
            temp = temp.right

            if temp is None:
                while stack:
                    temp = stack.pop()
                    # <---------- process node here --------> #
                    if not stack or temp != top(stack).right:    # temp is not right child
                        break
            else:
                curr = temp

        else:
            break

    return


def main():
    string = input()
    tree = BinaryTree.create_tree(string)
    print(tree)


if __name__ == '__main__':
    main()
