# python 3

def print_paths(root, target_sum, curr_sum, paths, path):
    if root is None:
        return

    curr_sum += root.data
    path.append(root.data)

    if curr_sum == target_sum:
        paths.append(path)

    print_paths(root.left, target_sum, curr_sum, paths, path.copy())
    print_paths(root.right, target_sum, curr_sum, paths, path.copy())

    return


# Find path sum equal to target from root to any node
def find_paths(root, target_sum):
    paths = []
    print_paths(root, target_sum, 0, paths, [])
    return paths


def main():
    pass


if __name__ == '__main__':
    main()
