# python 3

from itertools import permutations


def check_inclusion_brute_force(s1, s2):
    for perm in permutations(s1):
        if ''.join(perm) in s2:
            return True

    return False


def check_inclusion(s1: str, s2: str) -> bool:
    freq = {}
    char_count = len(s1)

    for char in s1:
        freq[char] = freq.get(char, 0) + 1

    for i in range(len(s2) - len(s1) + 1):
        j = i
        while j < len(s2) and s2[j] in freq and freq[s2[j]] != 0:
            freq[s2[j]] -= 1
            char_count -= 1
            j += 1

        j -= 1
        if char_count == 0:
            return True
        else:
            while j >= i:
                freq[s2[j]] += 1
                char_count += 1
                j -= 1

    return False


def main():
    s1 = 'ab'
    s2 = 'eidbaooo'

    print(check_inclusion_brute_force(s1, s2))


if __name__ == '__main__':
    main()
