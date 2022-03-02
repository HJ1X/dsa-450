# python 3
from trees.tree_basics import Node


def construct_tree_util(root, pre, pre_ln, n):
    if root[0] == n:
        return None

    new_node = Node(pre[root[0]])
    root[0] += 1

    if pre_ln[root[0] - 1] == 'N':
        new_node.left = construct_tree_util(root, pre, pre_ln, n)
        new_node.right = construct_tree_util(root, pre, pre_ln, n)

    return new_node


def construct_tree_recursive(pre, pre_ln, n):
    root = [0]
    return construct_tree_util(root, pre, pre_ln, n)


def construct_tree_iterative(pre, pre_ln, n):
    root = Node(pre[0])
    stack = [root]

    curr_node = root
    for i in range(1, n):
        new_node = Node(pre[i])

        if pre_ln[i - 1] == 'N':
            curr_node.left = new_node
            curr_node = new_node
            if pre_ln[i] != 'L':
                stack.append(new_node)

        elif stack:
            curr_node = stack.pop()
            curr_node.right = new_node

    return root


def main():
    pre = input().split()
    pre_ln = input().split()
    root = construct_tree_iterative(pre, pre_ln, len(pre))
    root.print_tree()


if __name__ == '__main__':
    main()
