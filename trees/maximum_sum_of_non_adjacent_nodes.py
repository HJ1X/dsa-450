# python 3

def get_max_adjacent_sum(root):
    if root is None:
        return 0, 0

    left_not_included, left_included = get_max_adjacent_sum(root.left)
    right_not_included, right_included = get_max_adjacent_sum(root.right)

    root_not_included = max(left_included,
                            right_included,
                            left_included + right_included,
                            left_not_included + right_not_included,
                            left_not_included + right_included,
                            left_included + right_not_included)

    root_included = max(root.data,
                        root.data + left_not_included,
                        root.data + right_not_included,
                        root.data + left_not_included + right_not_included)

    return root_not_included, root_included


def get_max_sum(root):
    return max(get_max_adjacent_sum(root))


def get_max_adjacent_sum_dp(root, dp):  # dp is a hash_map
    if root is None:
        return 0

    if root in dp:
        return dp[root]

    including = root.data
    if root.left:
        including += get_max_adjacent_sum_dp(root.left.left, dp)
        including += get_max_adjacent_sum_dp(root.left.right, dp)

    if root.right:
        including += get_max_adjacent_sum_dp(root.right.left, dp)
        including += get_max_adjacent_sum_dp(root.right.right, dp)

    excluding = 0
    excluding += get_max_adjacent_sum_dp(root.left, dp)
    excluding += get_max_adjacent_sum_dp(root.right, dp)

    dp[root] = max(including, excluding)
    return dp[root]


def main():
    pass


if __name__ == '__main__':
    main()
