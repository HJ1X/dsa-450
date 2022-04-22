# python 3

def find_sub_arrays(arr, n):
    count = 0
    freq_set = dict()
    prefix_sum = 0

    for i in range(n):
        prefix_sum += arr[i]
        if prefix_sum in freq_set:
            freq_set[prefix_sum] += 1
        else:
            freq_set[prefix_sum] = 1

    for key, value in freq_set.items():
        count += value * (value - 1) // 2    # nC2
        if key == 0:
            count += value

    return count


def main():
    pass


if __name__ == '__main__':
    main()