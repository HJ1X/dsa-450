# python 3

from collections import deque
from heap.heap_basics import Heap
from stacks_and_queues.queues.queue_with_max import QueueUsingStack


def max_of_subarrays_heap(arr, n, k):
    heap = Heap()
    for i in range(k):
        heap.insert(arr[i])

    ans = []
    for i in range(k, n):
        ans.append(heap.get_max())
        heap.remove(arr[i - k])
        heap.insert(arr[i])

    ans.append(heap.get_max())
    return ans


def max_of_subarrays_deque(arr, n, k):
    queue = deque()
    ans = []

    for i in range(n):
        # Removing element out of window
        if queue and queue[0] <= i - k:
            queue.popleft()

        # Removing irrelevant elements and then adding relevant element
        # i.e. elements in queue which are smaller than curr element
        while queue and arr[queue[-1]] <= arr[i]:
            queue.pop()
        queue.append(i)

        # Adding max element to ans
        if i >= k - 1:
            ans.append(arr[queue[0]])

    return ans


def max_of_subarrays_stacks_as_queue(arr, n, k):
    ans = []
    queue = QueueUsingStack()

    for i in range(n):
        queue.enque(arr[i])
        if i >= k-1:
            ans.append(queue.max())
            queue.deque()

    return ans


def main():
    arr = list(map(int, input().split()))
    k = int(input())
    print(max_of_subarrays_stacks_as_queue(arr, len(arr), k))


if __name__ == '__main__':
    main()
