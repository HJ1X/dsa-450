# python 3

# https://practice.geeksforgeeks.org/problems/sum-of-the-longest-bloodline-of-a-tree/1#
from trees.tree_basics import BinaryTree


def find_sum_paths(root, hash_map, curr_len, curr_sum):
    if root is None:
        return

    curr_len += 1
    curr_sum += root.data

    if root.left is None and root.right is None:
        if curr_len in hash_map:
            hash_map[curr_len].append(curr_sum)
        else:
            hash_map[curr_len] = [curr_sum]

    find_sum_paths(root.left, hash_map, curr_len, curr_sum)
    find_sum_paths(root.right, hash_map, curr_len, curr_sum)

    return


def sum_of_longest_path(root):
    hash_map = {}
    find_sum_paths(root, hash_map, 0, 0)

    max_len = -1
    max_val = None

    for length, sums in hash_map.items():
        if length > max_len:
            max_len = length
            max_val = max(sums)

    return max_val


def main():
    string = input()
    tree = BinaryTree.create_tree(string)
    print(sum_of_longest_path(tree.root))


if __name__ == '__main__':
    main()
