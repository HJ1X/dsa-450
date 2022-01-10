# Python 3
import collections


class Node:
    def __init__(self, val):
        self.key = val
        self.parent = None
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def find(self, key, root):
        if root is None:
            return None
        if root.key == key:
            return root
        elif root.key > key:
            if root.left is not None:
                return self.find(key, root.left)
            return root
        elif root.key < key:
            if root.right is not None:
                return self.find(key, root.right)
            return root

    def left_descendant(self, node):
        # returns the left most descendant of the given node
        if node.left is None:
            return node
        return self.left_descendant(node.left)

    def right_ancestor(self, node):
        # returns the first ancestor with greater value than node.key
        if node.parent is None:
            return None
        if node.parent.key > node.key:
            return node.parent
        return self.right_ancestor(node.parent)

    def next(self, node):
        if node.right:
            return self.left_descendant(node.right)
        else:
            return self.right_ancestor(node)

    def search_range(self, x, y):
        node = self.find(x, self.root)
        range_list = []
        while node.key <= y:
            if node.key >= x:
                range_list.append(node)
            node = self.next(node)
        return range_list

    def insert(self, key):
        node = self.find(key, self.root)
        new_node = Node(key)
        if node is None:
            self.root = new_node
            return
        if node.key > key:
            node.left = new_node
            new_node.parent = node
        else:
            node.right = new_node
            new_node.parent = node

    def delete(self, node):
        if node.right is None and node.left is None:
            if node.parent.left is node:
                node.parent.left = None
            else:
                node.parent.right = None
                return

        if node.right is None:
            node.left.parent = node.parent
            if node.parent.left is node:
                node.parent.left = node.left
            else:
                node.parent.right = node.left

            # if node.parent.key < node.left.key:
            #     node.parent.right = node.left
            # else:
            #     node.parent.left = node.left
        else:
            x = self.next(node)
            x.parent = node.parent
            if node.parent.left is node:
                node.parent.left = x
            else:
                node.parent.right = x

        del node

    def print_inorder(self, root):
        if not root:
            return
        self.print_inorder(root.left)
        print(root.key)
        self.print_inorder(root.right)

    def print_tree(self):
        # BFS traversal of tree
        if self.root is None:
            print('Empty tree')
            return
        q = collections.deque()
        q.appendleft(self.root)
        while q:
            node = q.pop()
            print(node.key)
            if node.left is not None:
                q.appendleft(node.left)
            if node.right is not None:
                q.appendleft(node.right)


def main():
    bst = BST()
    while 1:
        x = int(input())
        if x == 1:
            bst.insert(int(input()))
        elif x == 2:
            val = int(input())
            node = bst.find(val, bst.root)
            bst.delete(node)
        elif x == 3:
            bst.find(int(input()), bst.root)
        elif x == 4:
            val = int(input())
            node = bst.find(val, bst.root)
            bst.next(node)
        elif x == 5:
            x, y = map(int, input().split())
            bst.search_range(x, y)
        elif x == 6:
            # bst.print_tree()
            bst.print_inorder(bst.root)
        else:
            break


if __name__ == '__main__':
    main()

