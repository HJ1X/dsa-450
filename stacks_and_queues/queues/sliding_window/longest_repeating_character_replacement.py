# python 3
# Leetcode 424

def character_replacement_efficient(string: str, k: int) -> int:
    # O(n)
    max_len = 0
    hash_map = {}
    max_freq = 0

    l, r = 0, 0
    while r < len(string):
        curr_char = string[r]
        hash_map[curr_char] = hash_map.get(curr_char, 0) + 1
        max_freq = max(max_freq, hash_map[curr_char])

        window_len = r - l + 1

        if window_len - max_freq > k:
            hash_map[string[l]] -= 1
            l += 1
            window_len -= 1

        max_len = max(max_len, window_len)
        r += 1

    return max_len


def character_replacement(string: str, k: int) -> int:
    # O(26n)
    max_len = 0
    hash_map = {}
    max_freq = 0

    l, r = 0, 0
    while r < len(string):
        curr_char = string[r]
        hash_map[curr_char] = hash_map.get(curr_char, 0) + 1

        window_len = r - l + 1
        max_freq = max(hash_map.values())

        if window_len - max_freq > k:
            hash_map[string[l]] -= 1
            l += 1
            window_len -= 1

        max_len = max(max_len, window_len)
        r += 1

    return max_len


def main():
    string = input()
    k = int(input())
    print(character_replacement(string, k))


if __name__ == '__main__':
    main()
