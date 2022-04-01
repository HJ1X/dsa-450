# python 3

from collections import deque


def find_min_max(arr, k):
    n = len(arr)
    ans = 0

    queue_min = deque()
    queue_max = deque()

    for i in range(n):
        if queue_max and queue_max[0] <= i - k:
            queue_max.popleft()
        if queue_min and queue_min[0] <= i - k:
            queue_min.popleft()

        while queue_max and arr[queue_max[-1]] <= arr[i]:
            queue_max.pop()
        queue_max.append(i)

        while queue_min and arr[queue_min[-1]] >= arr[i]:
            queue_min.pop()
        queue_min.append(i)

        if i >= k - 1:
            ans += arr[queue_min[0]] + arr[queue_max[0]]

    return ans


def main():
    arr = list(map(int, input().split()))
    k = int(input())
    print(find_min_max(arr, k))


if __name__ == '__main__':
    main()
