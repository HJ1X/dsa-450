# python 3

def inorder_bottom_boundary(root, ans):
    if root is None:
        return

    inorder_bottom_boundary(root.left, ans)

    if root.left is None and root.right is None:
        ans.append(root.data)

    inorder_bottom_boundary(root.right, ans)
    return


def print_boundary_view(root):
    ans = [root.data]

    if root.left is None and root.right is None:
        return ans

    # Visiting left boundary
    if root.left:
        curr = root.left
        while True:
            if curr.left:
                ans.append(curr.data)
                curr = curr.left
            elif curr.right:
                ans.append(curr.data)
                curr = curr.right
            else:
                break

    # Visiting bottom boundary
    inorder_bottom_boundary(root, ans)

    # Visiting right boundary
    if root.right:
        stack = []
        curr = root
        while True:
            if curr.right:
                stack.append(curr.data)
                curr = curr.right
            elif curr.left:
                stack.append(curr.data)
                curr = curr.left
            else:
                break

        while stack:
            ans.append(stack.pop())
        ans.pop()  # removing root

    return ans


def main():
    pass


if __name__ == '__main__':
    main()
