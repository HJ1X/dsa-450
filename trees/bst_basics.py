# Python 3

from collections import deque as Deque
from trees.basic_functions_on_tree import height


class Node:
    def __init__(self, data):
        self.data = data
        self.parent = None
        self.height = 1
        self.left = None
        self.right = None

    def __repr__(self):
        return f'Node({self.data})'

    def appropriate_child(self, node, new_node):
        if self.left is node:
            self.left = new_node
        if self.right is node:
            self.right = new_node
        return

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


class BinarySearchTree:
    """
    Implements AVL Binary search tree
    """
    def __init__(self):
        self.root = None
        self.size = 0

    @staticmethod
    def serialize(root, arr):
        if root is None:
            return

        BinarySearchTree.serialize(root.left, arr)
        arr.append(str(root.data))
        BinarySearchTree.serialize(root.right, arr)

        return

    def __repr__(self):
        repr_arr = []
        self.serialize(self.root, repr_arr)
        repr_string = str(repr_arr)
        return repr_string

    def __str__(self):
        string = 'BST'

        inorder_arr = []
        self.serialize(self.root, inorder_arr)
        inorder_string = ' '.join(inorder_arr)

        string += f'({inorder_string})  Height: {height(self.root)}  Size: {self.size}'
        return string

    @staticmethod
    def __find(root, key):
        if root is None:
            return

        if root.data == key:
            return root
        elif root.data > key:
            return BinarySearchTree.__find(root.left, key)
        else:
            return BinarySearchTree.__find(root.right, key)

    @staticmethod
    def __find_place(root, key):
        if root is None:
            return

        if root.data == key:
            return root
        elif root.data > key:
            if root.left:
                return BinarySearchTree.__find_place(root.left, key)
            return root
        elif root.data < key:
            if root.right:
                return BinarySearchTree.__find_place(root.right, key)
            return root

    @staticmethod
    def _left_descendant(node):
        if node.left is None:
            return node
        else:
            return BinarySearchTree._left_descendant(node.left)

    @staticmethod
    def _right_ancestor(node):
        if node._parent is None:
            return None

        if node.key < node._parent.key:
            return node._parent
        else:
            return BinarySearchTree._right_ancestor(node._parent)

    @staticmethod
    def __adjust_height(node):
        if node is None:
            return

        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0

        node.height = 1 + max(left_height, right_height)
        return

    def __rotate_left(self, node):
        parent = node._parent
        left_child = node.left
        if left_child is None:
            return
        right_of_left = left_child.right

        left_child._parent = parent
        if parent:
            parent.appropriate_child(node, left_child)

        node._parent = left_child
        left_child.right = node

        node.left = right_of_left
        if right_of_left:
            right_of_left._parent = node

        if left_child._parent is None:
            self.root = left_child

        return

    def __rotate_right(self, node):
        parent = node._parent
        right_child = node.right
        if right_child is None:
            return
        left_of_right = right_child.left

        right_child._parent = parent
        if parent:
            parent.appropriate_child(node, right_child)

        node._parent = right_child
        right_child.left = node

        node.right = left_of_right
        if left_of_right:
            left_of_right._parent = node

        if right_child._parent is None:
            self.root = right_child

        return

    def __rebalance_right(self, node):
        left_node = node.left
        left_height_of_left = left_node.left.height if left_node.left else 0
        right_height_of_left = left_node.right.height if left_node.right else 0

        if left_height_of_left < right_height_of_left:
            self.__rotate_left(left_node)
            self.__adjust_height(left_node)
            self.__adjust_height(left_node.right)

        self.__rotate_left(node)
        self.__adjust_height(node)
        self.__adjust_height(node._parent)

    def __rebalance_left(self, node):
        right_node = node.right
        left_height_of_right = right_node.left.height if right_node.left else 0
        right_height_of_right = right_node.right.height if right_node.right else 0

        if right_height_of_right < left_height_of_right:
            self.__rotate_right(right_node)
            self.__adjust_height(right_node)
            self.__adjust_height(right_node.left)

        self.__rotate_right(node)
        self.__adjust_height(node)
        self.__adjust_height(node._parent)

    def __rebalance(self, node):
        if node is None:
            return

        parent = node.parent
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0

        if left_height > right_height + 1:
            self.__rebalance_right(node)
        if right_height > left_height + 1:
            self.__rebalance_left(node)
        self.__adjust_height(node)
        if parent:
            self.__rebalance(parent)
        return

    def __insert(self, key):
        """Basic insert procedure for Binary search trees"""
        node = self.find_place(key)
        new_node = Node(key)

        if node is None:  # Root node
            self.root = new_node
            return

        if node.data == key:  # Key already present in BST
            return

        if node.data < key:
            node.right = new_node
            new_node.parent = node
        else:
            node.left = new_node
            new_node.parent = node
        return

    def __delete(self, key):
        """
        :param key: Key of the node to be deleted
        :return: Return the old parent of node replacing deleted node
        """
        node = self.find(key)
        if not node:
            return

        if node.right is None:
            # promote node.left
            if node.left:
                node.left._parent = node.parent

            if node.parent:
                node.parent.appropriate_child(node, node.left)
            else:    # Root node is being deleted
                self.root = node.left
            return node.parent

        else:
            next_node = self.next(node)   # node.right = None condition has already been checked
            node.data = next_node.data

            # Promote next_node.right
            if next_node.right:
                next_node.right._parent = next_node.parent
            next_node.parent.appropriate_child(next_node, next_node.right)

            return next_node.parent

    # ------------------------------------------------ Main methods --------------------------------------------- #
    def find(self, key):
        """
        :param key: key to search
        :return: Node if found, else None
        """
        return self.__find(self.root, key)

    def find_place(self, key):
        """
        :param key: key to search
        :return: Node if found, else return node where key can be inserted
        """
        return self.__find_place(self.root, key)

    @staticmethod
    def next(node):
        """
        Takes input of node and not key. Find procedure should be used before to find node with key

        :param node: node of a BST
        :return: Node next to the given node
        """
        if node.right:
            return BinarySearchTree._left_descendant(node.right)
        else:
            return BinarySearchTree._right_ancestor(node)

    def range_search(self, start, end):
        """
        Searches nodes between given range inclusive

        :param start: lower limit of range
        :param end: upper limit of range
        :return: A list containing all the nodes keys in range in sorted order
        """
        if start > end:
            return None

        nodes_list = []
        node = self.find_place(start)

        while node.data <= end:
            if node.data >= start:
                nodes_list.append(node.data)
            node = self.next(node)

        return nodes_list

    def insert(self, key):
        self.__insert(key)
        self.size += 1
        node = self.find(key)
        self.__rebalance(node)

    def delete(self, key):
        node = self.__delete(key)
        self.size -= 1
        self.__rebalance(node)

    @classmethod
    def create_tree(cls, arr):
        bst = cls()
        for ele in arr:
            bst.insert(ele)

        return bst


def main():
    # arr = 1 2 3 4 5 6 7 9 12 34 56 76 23 67 478 736 463 87 47 76 3 64 25 73 78 63 45 09 63 545 55 46 31 4 1 16 15 11 0
    arr = list(map(int, input().split()))
    bst = BinarySearchTree.create_tree(arr)
    arr = list(map(int, input().split()))
    for ele in arr:
        bst.delete(ele)
    print(bst)
    bst.root.print_tree()


if __name__ == '__main__':
    main()
