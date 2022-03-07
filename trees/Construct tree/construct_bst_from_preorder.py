# python 3
from trees.tree_basics import Node
from sys import setrecursionlimit

setrecursionlimit(200000)


def construct_bst(arr, index, max_limit):
    """ The function assumes that given preorder traversal array represents a binary search tree """
    if index[0] == len(arr):
        return

    curr_data = arr[index[0]]

    if curr_data > max_limit:
        return

    root = Node(curr_data)
    index[0] += 1

    root.left = construct_bst(arr, index, curr_data)
    root.right = construct_bst(arr, index, max_limit)

    return root


def can_form_bst_util(arr, index, min_limit, max_limit):
    """ The function checks if the given preorder forms a bst """
    if index[0] == len(arr):
        return

    if min_limit <= arr[index[0]] <= max_limit:
        root_data = arr[index[0]]
        index[0] += 1

        can_form_bst_util(arr, index, min_limit, root_data)   # left subtree
        can_form_bst_util(arr, index, root_data, max_limit)   # right subtree


def can_form_bst(arr):
    index = [0]
    can_form_bst_util(arr, index, float('-inf'), float('inf'))

    if index[0] == len(arr):
        return 1
    else:
        return 0


def main():
    preorder = list(map(int, input().split()))
    # root = construct_bst(preorder, [0], float('inf'))
    # root.print_tree()
    print(can_form_bst(preorder))


if __name__ == '__main__':
    main()
