# python 3
# Array pair sum divisibility problem

def can_pair(nums, k):
    if len(nums) % 2 != 0:
        return False

    hash_map = {}
    for num in nums:
        hash_map[num % k] = hash_map.get(num % k, 0) + 1

    if 0 in hash_map and hash_map[0] % 2 != 0:
        return False

    for rem, count in hash_map.items():
        if rem == 0:
            continue

        if k - rem not in hash_map or hash_map[k - rem] != count:
            return False

    return True


def main():
    arr = list(map(int, input().split()))
    k = int(input())
    print(can_pair(arr, k))


if __name__ == '__main__':
    main()
