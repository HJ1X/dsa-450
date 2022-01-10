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

    def serialize_tree(self, root, hash_map):
        if root is None:
            return 'N'

        if not root.left and not root.right:
            return str(root.data)

        string = ''
        string += str(root.data)
        string += self.serialize_tree(root.left, hash_map)
        string += self.serialize_tree(root.right, hash_map)

        if string in hash_map:
            hash_map[string] += 1
        else:
            hash_map[string] = 1

        return string

    def find_duplicate_subtree(self, root):
        hash_map = {}
        self.serialize_tree(root, hash_map)

        print(hash_map)

        for key, value in hash_map.items():
            if value > 1:
                return 1
        return 0


def main():
    tree = Tree(1)
    tree.add_node(2, tree.root, 'l')
    tree.add_node(4, tree.root.left, 'l')
    tree.add_node(5, tree.root.left, 'r')
    tree.add_node(3, tree.root, 'r')
    tree.add_node(2, tree.root.right, 'r')
    tree.add_node(4, tree.root.right.right, 'l')
    tree.add_node(5, tree.root.right.right, 'r')
    tree.preorder(tree.root)
    tree.find_duplicate_subtree(tree.root)


if __name__ == '__main__':
    main()
