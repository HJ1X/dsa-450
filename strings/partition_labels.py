# python 3
# Leetcode - 763

def is_valid(string, index, hash_set):
    for i in range(index, len(string)):
        if string[i] in hash_set:
            return False
    return True


def find_partition(string, index, result):
    if index == len(string):
        return

    hash_set = set()
    for i in range(index, len(string)):
        hash_set.add(string[i])
        if is_valid(string, i + 1, hash_set):
            result.append(len(string[index: i + 1]))
            find_partition(string, i + 1, result)
            return


def partition_labels(s):
    result = []
    find_partition(s, 0, result)
    return result


def partition_labels_2(string):
    last_index = {}
    for i, char in enumerate(string):
        last_index[char] = i

    result = []
    partition_size = 0
    end = 0
    for i, char in enumerate(string):
        partition_size += 1
        end = max(last_index[char], end)

        if i == end:
            result.append(partition_size)
            partition_size = 0 

    return result


def main():
    string = input()
    # print(partition_labels(string))
    print(partition_labels_2(string))


if __name__ == '__main__':
    main()
