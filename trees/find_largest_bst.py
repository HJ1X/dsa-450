# python 3

from trees.tree_basics import BinaryTree


def find_largest_bst(root):
    if not root:
        return True, 0, float('inf'), float('-inf')

    is_bst_left, size_bst_left, min_val_left, max_val_left = find_largest_bst(root.left)
    is_bst_right, size_bst_right, min_val_right, max_val_right = find_largest_bst(root.right)

    if is_bst_left and is_bst_right and max_val_left < root.data and min_val_right:
        if max_val_left == float('-inf'):
            max_val_left = root.data
        if min_val_right == float('inf'):
            min_val_right = root.data
        return True, size_bst_left + size_bst_right + 1, max_val_left, min_val_right
    else:
        return False, max(size_bst_left, size_bst_right), 0, 0


def largest_bst_util(root):
    if root is None:
        return float('inf'), float('-inf'), 0

    min_left, max_left, left_size = largest_bst_util(root.left)
    min_right, max_right, right_size = largest_bst_util(root.right)

    if max_left < root.data < min_right:
        return max(max_left, root.data), min(min_right, root.data), 1 + left_size + right_size

    else:
        return float('inf'), float('-inf'), 1


def largest_bst(root):
    return largest_bst_util(root)[2]


def main():
    string = input()
    tree = BinaryTree.create_tree(string)
    print(find_largest_bst(tree.root))


if __name__ == '__main__':
    main()
