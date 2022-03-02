# python 3
from trees.tree_basics import Node


def construct_tree(string):
    if not string:
        return

    root = Node(int(string[0]))
    stack = [root]

    curr = root
    i = 1
    while i < len(string):
        if string[i] == '(':
            i += 1
            stack.append(curr)
            if curr.left is None:
                curr.left = Node(int(string[i]))
                curr = curr.left
            else:
                curr.right = Node(int(string[i]))
                curr = curr.right

        elif string[i] == ')':
            curr = stack.pop()

        i += 1
    return root


def main():
    string = input()
    root = construct_tree(string)
    root.print_tree()


if __name__ == '__main__':
    main()
