# python 3

from trees.bst_basics import BinarySearchTree
from trees.tree_basics import BinaryTree


def delete_node(root, data):
    if root is None:
        return root

    if data < root.data:
        root.left = delete_node(root.left, data)
    elif data > root.data:
        root.right = delete_node(root.right, data)
    else:
        if root.left is None:
            return root.right
        elif root.right is None:
            return root.left
        else:
            temp = BinarySearchTree.next(root.right)
            root.data = temp.data
            root.right = delete_node(root.right, temp.data)

    return root


def next_node(node, direction):
    nxt_node = node.left if direction == 'l' else node.right
    if nxt_node is None:
        return node
    else:
        return next_node(nxt_node, direction)


def inorder_successor_and_predecessor_util(root, successor, predecessor, key):
    if root is None:
        return successor, predecessor

    if root.data == key:
        if root.right:
            successor = next_node(root.right, 'l')
        if root.left:
            predecessor = next_node(root.left, 'r')
        return successor, predecessor

    if root.data < key:
        predecessor = root.data
        return inorder_successor_and_predecessor_util(root.right, successor, predecessor, key)
    else:
        successor = root.data
        return inorder_successor_and_predecessor_util(root.left, successor, predecessor, key)


def inorder_successor_and_predecessor(root, key):
    return inorder_successor_and_predecessor_util(root, -1, -1, key)


def is_bst_inorder(root):
    stack = []
    curr = root
    prev = float('-inf')

    while True:
        if curr:
            stack.append(curr)
            curr = curr.left

        elif stack:
            curr = stack.pop()
            if curr.data <= prev:
                return False

            prev = curr.data
            curr = curr.right

        else:
            break

    return True


def is_bst_recursive_util(root, min_val, max_value):
    if root is None:
        return True

    if root.data <= min_val or root.data >= max_value:
        return False

    return (is_bst_recursive_util(root.left, min_val, root.data) and
            is_bst_recursive_util(root.right, root.data, max_value))


def is_bst_recursive(root):
    if is_bst_recursive_util(root, float('-inf'), float('inf')):
        return True
    else:
        return False


def main():
    # bst = BinarySearchTree.create_tree([50, 20, 60, 10, 30, 55, 70])
    # print(inorder_successor_and_predecessor(bst.root, 1))
    string = input()
    tree = BinaryTree.create_tree(string)
    print(is_bst_recursive(tree.root))


if __name__ == '__main__':
    main()
