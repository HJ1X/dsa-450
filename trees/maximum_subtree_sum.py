# python 3
from trees.tree_basics import BinaryTree


def find_max_sum(root, max_sum):
    if root is None:
        return 0

    if root.left is None and root.right is None:
        return root.data

    left_sum = find_max_sum(root.left, max_sum)
    right_sum = find_max_sum(root.right, max_sum)

    curr_sum = left_sum + right_sum + root.data
    if curr_sum > max_sum:
        max_sum = curr_sum

    return max_sum


def main():
    string = input()
    tree = BinaryTree.create_tree(string)
    print(find_max_sum(tree.root, float('-inf')))


if __name__ == '__main__':
    main()
