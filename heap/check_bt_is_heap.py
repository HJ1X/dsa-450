# python 3
from collections import deque

from trees.basic_functions_on_tree import is_complete
from trees.tree_basics import BinaryTree


def is_heap_util(root):
    if root is None:
        return True

    left = is_heap_util(root.left)
    right = is_heap_util(root.right)

    if not left or not right:
        return False

    if root.left and root.left.data > root.data:
        return False

    if root.right and root.right.data > root.data:
        return False

    return True


def is_heap(root):
    if is_heap_util(root) and is_complete(root):
        return True
    else:
        return False


def is_heap_efficient(root):
    queue = deque()
    queue.append(root)

    should_be_leaf = False

    while queue:
        node = queue.popleft()

        # Processing left child
        if node.left:
            if should_be_leaf or node.left.data >= node.data:
                return False
            else:
                queue.append(node.left)
        else:
            should_be_leaf = True

        # Processing right child
        if node.right:
            if should_be_leaf or node.right.data >= node.data:
                return False
            else:
                queue.append(node.right)
        else:
            should_be_leaf = True

    return True


def main():
    string = input()
    tree = BinaryTree.create_tree(string)
    print(is_heap(tree.root))


if __name__ == '__main__':
    main()
