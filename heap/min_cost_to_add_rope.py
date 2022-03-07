# python 3
from heapq import heappush, heappop


def min_cost(arr):
    heap = []
    for ele in arr:
        heappush(heap, ele)

    total_cost = 0
    while len(heap) > 1:
        rope1 = heappop(heap)
        rope2 = heappop(heap)

        new_rope = rope1 + rope2
        total_cost += new_rope

        heappush(heap, new_rope)

    return total_cost


def main():
    pass


if __name__ == '__main__':
    main()
