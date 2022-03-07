# python 3

# Function to return the k-largest elements from an array.

# This approach is good if we want to print the k-largest element else, if we only need to find the kth-largest
# element than, quick select approach is better - TC - O(N) average

# This approach creates max-heap from entire array, and they extract max k times so, TC = n + klogn
# Better approach is to just create a min-heap of size k and use it. (on gfg practice)  TC = O((n-k)log(k))

from heap.heap_basics import Heap


def k_largest(arr, k):
    res = []
    heap = Heap(arr)

    for i in range(k):
        res.append(heap.extract_max())

    return res


def main():
    k = int(input())
    arr = list(map(int, input().split()))
    print(*k_largest(arr, k))


if __name__ == '__main__':
    main()
