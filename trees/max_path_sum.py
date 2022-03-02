# python 3

def max_sum_of_paths(self, root):
    if root is None:
        return 0

    left = self.max_sum_of_paths(root.left)
    right = self.max_sum_of_paths(root.right)

    return max(left + root.data, right + root.data)


def main():
    pass


if __name__ == '__main__':
    main()
