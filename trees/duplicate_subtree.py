# python 3

def serialize_tree(root, hash_map):
    if root is None:
        return 'N'

    if root.left is None and root.right is None:
        return str(root.data)

    string = ''
    string += str(root.data)
    string += serialize_tree(root.left, hash_map)
    string += serialize_tree(root.right, hash_map)

    if string in hash_map:
        hash_map[string] += 1
    else:
        hash_map[string] = 1

    return string


def check_duplicate_subtree(root):
    hash_map = {}
    serialize_tree(root, hash_map)

    for key, value in hash_map.items():
        if value > 1:
            return 1
    return 0


def main():
    pass


if __name__ == '__main__':
    main()
