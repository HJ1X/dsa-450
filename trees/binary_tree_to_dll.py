# python 3

# https://practice.geeksforgeeks.org/problems/binary-tree-to-dll/1#

from linked_list.double_linked_list_class import Node


def binary_tree_to_dll(root):
    head = Node(-1)
    curr_list = head

    stack = []
    curr = root

    while True:
        if curr is not None:
            stack.append(curr)
            curr = curr.left

        elif stack:
            curr = stack.pop()

            new_node = Node(curr.data)
            curr_list.next = new_node
            new_node.prev = curr_list
            curr_list = new_node

            curr = curr.right

        else:
            break

    head = head.next
    head.prev = None

    return head


def main():
    pass


if __name__ == '__main__':
    main()
