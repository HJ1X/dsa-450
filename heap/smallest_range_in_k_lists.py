# python 3
from heapq import heappush, heappop


def smallest_range(arr, k):
    heap = []
    min_element = float('inf')
    max_element = float('-inf')

    for i in range(k):
        curr_element = arr[i].pop(0)
        heappush(heap, (curr_element, i))

        if curr_element > max_element:
            max_element = curr_element

        if curr_element < min_element:
            min_element = curr_element

    min_range = min_element, max_element

    while heap:
        curr_element, index = heappop(heap)

        if not arr[index]:
            return min_range

        new_element = arr[index].pop(0)
        heappush(heap, (new_element, index))

        min_element = heap[0][0]
        max_element = max(max_element, new_element)

        curr_range = max_element - min_element
        if curr_range < min_range[1] - min_range[0]:
            min_range = min_element, max_element

    return min_range


def main():
    arr = [[1, 2, 3, 4],
           [5, 6, 7, 8],
           [9, 10, 11, 12]]
    print(smallest_range(arr, 3))


if __name__ == '__main__':
    main()
