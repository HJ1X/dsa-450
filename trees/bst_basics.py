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
            if root.left is not None:
                return BinarySearchTree.__find_place(root.left, key)
            return root
        elif root.data < key:
            if root.right is not None:
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
        if node.parent is None:
            return None

        if node.key < node.parent.key:
            return node.parent
        else:
            return BinarySearchTree._right_ancestor(node.parent)

    @staticmethod
    def __adjust_height(node):
        if node is None:
            return

        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0

        node.height = 1 + max(left_height, right_height)
        return

    def __rotate_left(self, node):
        parent = node.parent
        left_child = node.left
        if left_child is None:
            return
        right_of_left = left_child.right

        left_child.parent = parent
        if parent is not None:
            parent.appropriate_child(node, left_child)

        node.parent = left_child
        left_child.right = node

        node.left = right_of_left
        if right_of_left is not None:
            right_of_left.parent = node

        if left_child.parent is None:
            self.root = left_child

        return

    def __rotate_right(self, node):
        parent = node.parent
        right_child = node.right
        if right_child is None:
            return
        left_of_right = right_child.left

        right_child.parent = parent
        if parent is not None:
            parent.appropriate_child(node, right_child)

        node.parent = right_child
        right_child.left = node

        node.right = left_of_right
        if left_of_right is not None:
            left_of_right.parent = node

        if right_child.parent is None:
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
        self.__adjust_height(node.parent)

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
        self.__adjust_height(node.parent)

    def __rebalance(self, node):
        parent = node.parent
        left_height = node.left.height if node.left else 0
        right_height = node.right.height if node.right else 0

        if left_height > right_height + 1:
            self.__rebalance_right(node)
        if right_height > left_height + 1:
            self.__rebalance_left(node)
        self.__adjust_height(node)
        if parent is not None:
            self.__rebalance(parent)
        return

    def __insert(self, key):
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
        :return: Key of node next to the given node
        """
        if node.right is not None:
            return BinarySearchTree._left_descendant(node.right).data
        else:
            return BinarySearchTree._right_ancestor(node).data

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
        node = self.find(key)
        if not node:
            return

        if node.right is None:
            # promote node.left
            node.left.parent = node.parent
            node.parent.appropriate_child(node, node.left)

        else:
            next_node = self.next(node)     # node.right = None condition has already been checked
            node.data = next_node.data

            # Promote next_node.right
            next_node.right.parent = next_node.parent
            next_node.parent.left = next_node.right      # next_node is definitely left child

        return

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
    print(bst)
    bst.root.print_tree()


if __name__ == '__main__':
    main()

    # def find(self, key, root):
    #     if root is None:
    #         return None
    #     if root.key == key:
    #         return root
    #     elif root.key > key:
    #         if root.left is not None:
    #             return self.find(key, root.left)
    #         return root
    #     elif root.key < key:
    #         if root.right is not None:
    #             return self.find(key, root.right)
    #         return root
    #
    # def left_descendant(self, node):
    #     # returns the left most descendant of the given node
    #     if node.left is None:
    #         return node
    #     return self.left_descendant(node.left)
    #
    # def right_ancestor(self, node):
    #     # returns the first ancestor with greater value than node.key
    #     if node.parent is None:
    #         return None
    #     if node.parent.key > node.key:
    #         return node.parent
    #     return self.right_ancestor(node.parent)
    #
    # def next(self, node):
    #     if node.right:
    #         return self.left_descendant(node.right)
    #     else:
    #         return self.right_ancestor(node)
    #
    # def search_range(self, x, y):
    #     node = self.find(x, self.root)
    #     range_list = []
    #     while node.key <= y:
    #         if node.key >= x:
    #             range_list.append(node)
    #         node = self.next(node)
    #     return range_list
    #
    # def insert(self, key):
    #     node = self.find(key, self.root)
    #     new_node = Node(key)
    #     if node is None:
    #         self.root = new_node
    #         return
    #     if node.key > key:
    #         node.left = new_node
    #         new_node.parent = node
    #     else:
    #         node.right = new_node
    #         new_node.parent = node
    #
    # def delete(self, node):
    #     if node.right is None and node.left is None:
    #         if node.parent.left is node:
    #             node.parent.left = None
    #         else:
    #             node.parent.right = None
    #             return
    #
    #     if node.right is None:
    #         node.left.parent = node.parent
    #         if node.parent.left is node:
    #             node.parent.left = node.left
    #         else:
    #             node.parent.right = node.left
    #
    #         # if node.parent.key < node.left.key:
    #         #     node.parent.right = node.left
    #         # else:
    #         #     node.parent.left = node.left
    #     else:
    #         x = self.next(node)
    #         x.parent = node.parent
    #         if node.parent.left is node:
    #             node.parent.left = x
    #         else:
    #             node.parent.right = x
    #
    #     del node
    #
    # def print_inorder(self, root):
    #     if not root:
    #         return
    #     self.print_inorder(root.left)
    #     print(root.key)
    #     self.print_inorder(root.right)
    #
    # def print_tree(self):
    #     # BFS traversal of tree
    #     if self.root is None:
    #         print('Empty tree')
    #         return
    #     q = collections.deque()
    #     q.appendleft(self.root)
    #     while q:
    #         node = q.pop()
    #         print(node.key)
    #         if node.left is not None:
    #             q.appendleft(node.left)
    #         if node.right is not None:
    #             q.appendleft(node.right)
