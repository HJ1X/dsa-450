# python 3

from collections import deque as Deque


class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    def __repr__(self):
        return f'Node({self.data})'

    def print_tree(self):
        deque = Deque()
        deque.appendleft(self)

        while deque:
            n = len(deque)
            for i in range(n):
                node = deque.pop()
                print(node.data, end=' ')

                if node.left:
                    deque.appendleft(node.left)
                if node.right:
                    deque.appendleft(node.right)

            print()


class BinaryTree:
    def __init__(self):
        self.root = None

    @staticmethod
    def serialize(root, arr):
        if root is None:
            return

        BinaryTree.serialize(root.left, arr)
        arr.append(str(root.data))
        BinaryTree.serialize(root.right, arr)

        return

    def __repr__(self):
        # Inorder serialization
        repr_arr = []
        self.serialize(self.root, repr_arr)
        repr_string = ' '.join(repr_arr)
        return repr_string

    def __str__(self):
        deque = Deque()
        deque.appendleft(self.root)

        str_value = ''
        while deque:
            n = len(deque)
            for i in range(n):
                node = deque.pop()
                str_value += str(node.data) + ' '

                if node.left:
                    deque.appendleft(node.left)
                if node.right:
                    deque.appendleft(node.right)

            str_value += '\n'

        return str_value

    @staticmethod
    def __create_list(string):
        if not string:
            return None

        nodes_list = string.split()
        for i in range(len(nodes_list)):
            if nodes_list[i].lower() == 'n':
                nodes_list[i] = None
            else:
                nodes_list[i] = Node(int(nodes_list[i]))

        return nodes_list

    @classmethod
    def create_tree(cls, string):
        nodes_list = cls.__create_list(string)
        if nodes_list is None:
            return 'Empty String provided'

        deque = Deque()
        root = nodes_list[0]
        deque.appendleft(root)

        i = 1
        while deque and i < len(nodes_list):
            curr_node = deque.pop()

            left_node = nodes_list[i]
            if left_node is not None:
                curr_node.left = left_node
                deque.appendleft(left_node)

            i += 1
            if i == len(nodes_list):
                break

            right_node = nodes_list[i]
            if right_node is not None:
                curr_node.right = right_node
                deque.appendleft(right_node)

            i += 1

        new_tree = cls()
        new_tree.root = root
        return new_tree


def main():
    string = input()
    tree = BinaryTree.create_tree(string)
    print(tree)
    print(repr(tree))


if __name__ == '__main__':
    main()
