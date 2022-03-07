# python 3

def morris_inorder(root):
    curr = root
    while curr:
        if curr.left is None:
            # <----------- Process node here ----------- >
            curr = curr.right

        else:
            prev = curr.left                                # Calculating right descendant of curr.left
            while prev.right and prev.right is not curr:    # to create a thread from it to curr node, i.e.
                prev = prev.right                           # root node

            if prev.right is None:                          # creating thread
                prev.right = curr
                curr = curr.left
            else:                                           # Removing thread
                prev.right = None
                # <----------- Process node here ----------- >
                curr = curr.right

    return


def main():
    pass


if __name__ == '__main__':
    main()
