# python 3

def smallest_window_substring(string, pattern):
    if len(pattern) > len(string):
        return -1

    n = len(string)

    hash_map = {}
    for char in pattern:
        hash_map[char] = hash_map.get(char, 0) + 1

    count = len(hash_map)  # Stores count of distinct characters in pattern
    i, j = 0, 0

    min_len_ans = float('inf')
    ans_str = ''

    while j < n:
        end_char = string[j]
        j += 1

        if end_char in hash_map:
            hash_map[end_char] -= 1
            if hash_map[end_char] == 0:
                count -= 1

        # If all the characters are found increment i to remove unwanted
        # characters i.e. till count becomes > 0
        while count == 0:
            start_char = string[i]
            i += 1

            if start_char in hash_map:
                hash_map[start_char] += 1
                if hash_map[start_char] > 0:
                    count += 1

            if min_len_ans > j - i:
                min_len_ans = j - i
                ans_str = string[i - 1:j]

    if min_len_ans == float('inf'):
        return -1
    else:
        return ans_str


def find_minimum_window_substring(string, pattern):
    n = len(string)

    if len(pattern) > n:
        return -1

    hash_pattern = {}
    for char in pattern:
        hash_pattern[char] = hash_pattern.get(char, 0) + 1

    hash_map_window = {char: 0 for char in hash_pattern.keys()}

    count_needed = len(hash_pattern)
    curr_count = 0

    min_len_ans = float('inf')
    ans = ''

    i, j = 0, 0
    while j < n:
        end_char = string[j]
        j += 1

        if end_char in hash_map_window:
            hash_map_window[end_char] += 1
            if hash_map_window[end_char] == hash_pattern[end_char]:
                curr_count += 1

        while curr_count == count_needed:
            start_char = string[i]
            i += 1

            if start_char in hash_map_window:
                hash_map_window[start_char] -= 1
                if hash_map_window[start_char] < hash_pattern[start_char]:
                    curr_count -= 1

            if j - i < min_len_ans:
                min_len_ans = j - i
                ans = string[i-1: j]

    if min_len_ans == float('inf'):
        return -1
    else:
        return ans


def main():
    string = input()
    pattern = input()
    print(find_minimum_window_substring(string, pattern))


if __name__ == '__main__':
    main()
