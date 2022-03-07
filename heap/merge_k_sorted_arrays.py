# python 3

from heapq import heappush, heappop


def merge_k_arrays(arr, k):
    heap = []
    for i in range(k):
        heappush(heap, (arr[i].pop(0), i))
    ans = []
    while heap:
        val = heappop(heap)
        ans.append(val[0])
        if arr[val[1]]:
            heappush(heap, (arr[val[1]].pop(0), val[1]))
    return ans


def main():
    pass


if __name__ == '__main__':
    main()
