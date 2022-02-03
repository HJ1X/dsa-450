# python 3


def find_min_jumps(arr):
    n = len(arr)

    jumps = 0
    max_reachable = 0
    steps = 0

    for i in range(n):
        if i == n - 1:
            return jumps

        max_reachable = max(max_reachable, i + arr[i])
        steps -= 1

        if steps <= 0:
            jumps += 1
            if max_reachable <= i:
                return -1

            steps = max_reachable - i


def find_min_jumps_dp(arr):
    n = len(arr)

    min_jumps = [0 for i in range(n)]
    for i in range(n - 2, -1, -1):
        if i + arr[i] <= n:
            min_jumps[i] = 1

        else:
            min_jump_from_i = float('inf')
            max_reachable = i + arr[i]

            for j in range(i + 1, max_reachable + 1):
                curr_min_jump = min_jumps[j] + 1
                if curr_min_jump < min_jump_from_i:
                    min_jump_from_i = curr_min_jump

            min_jumps[i] = min_jump_from_i

    return min_jumps[0]


def main():
    arr = list(map(int, input().split()))
    print(find_min_jumps(arr))


if __name__ == '__main__':
    main()
