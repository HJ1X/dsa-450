# python 3

from itertools import permutations as permutation


# ------------------------------------------------------------------------------------------------------------------ #
def find_permutations_itertools(self, S):
    S = sorted(S)         # sorted function already creates list from string
    return list(map(''.join, permutation(S)))


# ------------------------------------------------------------------------------------------------------------------- #
def generate_permutations(arr, i, permutations):
    """
    For every j from 0 to len(arr):
    fix character j ot ith position i.e.
    swap arr[i] and arr[j] and then
    permute remaining string
    https://media.geeksforgeeks.org/wp-content/cdn-uploads/NewPermutation.gif
    """
    if i == len(arr)-1:
        permutations.append(''.join(arr))
        return

    # Fix jth element at i and then recurse
    for j in range(i, len(arr)):
        arr[i], arr[j] = arr[j], arr[i]
        generate_permutations(arr, i+1, permutations)
        arr[i], arr[j] = arr[j], arr[i]


def find_permutations(string):
    permutations = []
    generate_permutations(list(string), 0, permutations)
    permutations.sort()
    return permutations


# ------------------------------------------------------------------------------------------------------------------ #
def generate_permutations_lexi(string, answer, permutations):
    if not string:
        permutations.append(answer)
        return

    for i in range(len(string)):
        char = string[i]

        left_str = string[:i]
        right_str = string[i + 1:]
        remain_str = left_str + right_str

        generate_permutations(remain_str, answer + char, permutations)


def find_permutations_lexi(self, S):
    S = ''.join(sorted(S))
    permutations = []
    generate_permutations(S, '', permutations)
    return permutations


# ------------------------------------------------------------------------------------------------------------------ #
def main():
    string = input()
    print(find_permutations(string))


if __name__ == '__main__':
    main()
