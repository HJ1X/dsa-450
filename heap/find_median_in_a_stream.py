# python 3
from heapq import heappop, heappush

min_heap = []
max_heap = []


def balance_heaps():
    if len(max_heap) > len(min_heap):
        ele = -heappop(max_heap)
        heappush(min_heap, ele)
    else:
        ele = heappop(min_heap)
        heappush(max_heap, -ele)


def get_median():
    if len(max_heap) == len(min_heap):
        val = (-max_heap[0] + min_heap[0]) / 2
        if val.is_integer():
            return int(val)
        else:
            return val

    elif len(max_heap) > len(min_heap):
        return -max_heap[0]

    else:
        return min_heap[0]


def insert_heaps(x):
    if not max_heap and not min_heap:
        heappush(max_heap, -x)
    elif -x >= max_heap[0]:
        heappush(max_heap, -x)
    else:
        heappush(min_heap, x)

    if abs(len(min_heap) - len(max_heap)) > 1:
        balance_heaps()

    return


def main():
    arr = list(map(int, input().split()))
    for ele in arr:
        insert_heaps(ele)
        print(get_median())


if __name__ == '__main__':
    main()
