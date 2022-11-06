# python 3

def find_distinct_elements_count(arr, n, k):
    hash_map = {}
    count = 0
    ans = []

    for i in range(k):
        ele = arr[i]

        if ele not in hash_map:
            hash_map[ele] = 1
            count += 1
        else:
            hash_map[ele] += 1

    ans.append(count)

    for i in range(k, n):
        new_ele = arr[i]
        prev_ele = arr[i - k]

        if hash_map[prev_ele] == 1:
            count -= 1
        hash_map[prev_ele] -= 1

        if new_ele not in hash_map or hash_map[new_ele] == 0:
            count += 1
        hash_map[new_ele] = hash_map.get(new_ele, 0) + 1

        ans.append(count)

    return ans


def main():
    arr = list(map(int, input().split()))
    k = int(input())
    print(find_distinct_elements_count(arr, len(arr), k))


if __name__ == '__main__':
    main()
