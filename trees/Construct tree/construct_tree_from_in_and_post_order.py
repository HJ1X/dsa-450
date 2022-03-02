# python 3
from trees.tree_basics import Node


def build_tree(inorder, postorder, n):
    if not inorder:
        return

    root = Node(postorder[-1])
    index = inorder.index(root.data)

    new_inorder_left = inorder[:index]
    new_inorder_right = inorder[index + 1:]

    new_postorder_left = postorder[:index]
    new_postorder_right = postorder[index:len(postorder) - 1]

    root.left = build_tree(new_inorder_left, new_postorder_left, n)
    root.right = build_tree(new_inorder_right, new_postorder_right, n)

    return root


def main():
    inorder = [4, 8, 2, 5, 1, 6, 3, 7]
    postorder = [8, 4, 5, 2, 6, 7, 3, 1]
    build_tree(inorder, postorder, len(postorder))


if __name__ == "__main__":
    main()
