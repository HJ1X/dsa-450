# python 3

from trees.tree_basics import BinaryTree, Node


def serialize_tree(root, arr):
    if root is None:
        arr.append(-1)
        return

    arr.append(root.data)
    serialize_tree(root.left, arr)
    serialize_tree(root.right, arr)


def deserialize_util(arr, index):
    if index == len(arr) or arr[index] == -1:
        return None, index

    root = Node(arr[index])
    root.left, index = deserialize_util(arr, index + 1)
    root.right, index = deserialize_util(arr, index + 1)

    return root, index


def deserialize_tree(arr):
    return deserialize_util(arr, 0)[0]


def main():
    string = input()
    tree = BinaryTree.create_tree(string)
    arr = []
    print(serialize_tree(tree.root, arr))
    deserialize_tree(arr).print_tree()


if __name__ == '__main__':
    main()
