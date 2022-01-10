# python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class Tree:
    def __init__(self, data):
        self.root = Node(data)

    def add_node(self, data, node, where):
        if where == 'l':
            node.left = Node(data)
        if where == 'r':
            node.right = Node(data)

    def preorder(self, root):
        if root is None:
            return

        print(root.data, end=' ')
        self.preorder(root.left)
        self.preorder(root.right)

    def largest_bst(self, root):
        # code here
        if not root:
            return True, 0, float('inf'), float('-inf')

        # if not root.left and not root.right:
        #     return True, 1, root.data, root.data

        is_bst_left, size_bst_left, min_val_left, max_val_left = self.largest_bst(root.left)
        is_bst_right, size_bst_right, min_val_right, max_val_right = self.largest_bst(root.right)

        if is_bst_left and max_val_left < root.data and is_bst_right and min_val_right > root.data:
            if max_val_left == float('-inf'):
                max_val_left = root.data
            if min_val_right == float('inf'):
                min_val_right = root.data
            return True, size_bst_left + size_bst_right + 1, max_val_left, min_val_right

        else:
            return False, max(size_bst_left, size_bst_right), 0, 0


def main():
    tree = Tree(6)
    tree.add_node(6, tree.root, 'l')
    tree.add_node(2, tree.root.left, 'r')
    tree.add_node(8, tree.root.left.right, 'r')
    tree.add_node(3, tree.root, 'r')
    tree.add_node(9, tree.root.right, 'l')
    tree.add_node(3, tree.root.right, 'r')
    tree.add_node(8, tree.root.right.left, 'l')
    tree.add_node(2, tree.root.right.left, 'r')
    tree.preorder(tree.root)
    print(tree.largest_bst(tree.root))


if __name__ == '__main__':
    main()
