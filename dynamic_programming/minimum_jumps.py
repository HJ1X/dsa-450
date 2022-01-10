# python 3

def find_min_jumps(arr):
    n = len(arr)
    if arr[0] == 0:
        return -1

    max_reach = arr[0]
    steps = arr[0]
    jumps = 0
    for i in range(1, n):
        steps -= 1
        max_reach = max(max_reach, arr[i] + i)
        if steps == 0:
            jumps += 1
            if i >= max_reach:
                return -1
            steps = max_reach - i
    return jumps


def main():
    arr = list(map(int, input().split()))
    print(find_min_jumps(arr))


if __name__ == '__main__':
    main()
