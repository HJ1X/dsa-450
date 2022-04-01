# python 3

def is_palindrome(string, start, end):
    while start < end:
        if string[start] != string[end]:
            return False

        start += 1
        end -= 1

    return True


def find_partition_util(string, start, partition, res):
    if start == len(string):
        res.append(partition.copy())
        return

    for end in range(start, len(string)):
        if is_palindrome(string, start, end):
            partition.append(string[start:end + 1])
            find_partition_util(string, end + 1, partition, res)
            partition.pop()


def find_partitions(string):
    res = []
    partition = []

    find_partition_util(string, 0, partition, res)
    return res


def main():
    string = input()
    print(find_partitions(string))


if __name__ == '__main__':
    main()
