# python 3

def count_set_bits(n):
    count = 0
    i = 2

    while (i // 2) < (n + 1):
        num_patterns_present = (n + 1) // i
        num_1s_in_pattern = i // 2
        count += num_patterns_present * num_1s_in_pattern

        remaining_nums = (n + 1) % i
        num_0s_in_pattern = i // 2
        if num_0s_in_pattern < remaining_nums:
            count += remaining_nums - num_0s_in_pattern

        i *= 2

    return count


def main():
    n = int(input())
    print(count_set_bits(n))


if __name__ == '__main__':
    main()
