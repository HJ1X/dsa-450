# python 3

def inorder(root, arr):
    if root is None:
        return

    inorder(root.left, arr)
    arr.append(root.data)
    inorder(root.right, arr)

    return arr


def count_pairs(root1, root2, x):
    arr1 = inorder(root1, [])
    arr2 = inorder(root2, [])

    i, j = 0, len(arr2) - 1
    count = 0

    while i < len(arr1) and j >= 0:
        if arr1[i] + arr2[j] == x:
            count += 1

        if arr1[i] + arr2[j] > x:
            j -= 1
        else:
            i += 1

    return count


def main():
    pass


if __name__ == '__main__':
    main()
