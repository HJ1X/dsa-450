# python 3
from trees.tree_basics import Node


def construct_tree(inorder, preorder):
    if not inorder:
        return

    root = Node(preorder[0])
    index_root_inorder = inorder.index(root.data)

    root.left = construct_tree(
        inorder[:index_root_inorder],
        preorder[1:index_root_inorder + 1],
    )
    root.right = construct_tree(
        inorder[index_root_inorder + 1:],
        preorder[1 + index_root_inorder:],
    )

    return root


def construct_tree_util(inorder, in_start, in_end, preorder, pre_start, hash_map):
    # No node left
    if in_start > in_end:
        return

    root = Node(preorder[pre_start])

    in_root = hash_map[root.data]
    nodes_left = in_root - in_start

    root.left = construct_tree_util(
        inorder, in_start, in_root - 1,
        preorder, pre_start + 1,
        hash_map)
    root.right = construct_tree_util(
        inorder, in_root + 1, in_end,
        preorder, pre_start + nodes_left + 1,
        hash_map)

    return root


def construct_tree_efficient(inorder, preorder, n):
    # Hashing values for faster access
    hash_map = {inorder[i]: i for i in range(n)}

    return construct_tree_util(inorder, 0, n-1, preorder, 0, hash_map)


def main():
    inorder = [3, 1, 4, 0, 5, 2]
    preorder = [0, 1, 3, 4, 2, 5]
    n = 6
    root1 = construct_tree(inorder, preorder)
    root2 = construct_tree_efficient(inorder, preorder, n)

    root1.print_tree()
    root2.print_tree()


if __name__ == '__main__':
    main()
