# python 3

from collections import deque


def print_first_negative(arr, n, k):
    queue = deque()
    ans = []

    for i in range(n):
        if queue and queue[0] <= i - k:
            queue.popleft()

        if arr[i] < 0:
            queue.append(i)

        if i >= k - 1:
            if queue:
                ans.append(arr[queue[0]])
            else:
                ans.append(0)

    return ans


def main():
    pass


if __name__ == '__main__':
    main()
