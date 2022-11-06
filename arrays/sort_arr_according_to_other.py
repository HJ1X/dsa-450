# python 3

def relative_sort(arr1, n, arr2, m):
    hash_map = {}
    for ele in arr1:
        hash_map[ele] = hash_map.get(ele, 0) + 1

    ptr_to_add_ele = 0
    for ele in arr2:
        if ele in hash_map:
            for i in range(hash_map[ele]):
                arr1[ptr_to_add_ele] = ele
                ptr_to_add_ele += 1

            hash_map.pop(ele)

    hash_map = dict(sorted(hash_map.items()))
    for key, value in hash_map.items():
        for i in range(value):
            arr1[ptr_to_add_ele] = key
            ptr_to_add_ele += 1

    return arr1


def main():
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))

    print(relative_sort(arr1, len(arr1), arr2, len(arr2)))


if __name__ == '__main__':
    main()
