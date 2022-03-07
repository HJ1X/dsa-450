# python 3


def _parent(i):
    return (i-1) // 2


def _left_child(i):
    return (2*i) + 1


def _right_child(i):
    return (2*i) + 2


def _sift_up(arr, i):
    while i > 0 and arr[_parent(i)] < arr[i]:
        arr[_parent(i)], arr[i] = arr[i], arr[_parent(i)]
        i = _parent(i)


def _sift_down(arr, i, size):
    max_index = i

    l = _left_child(i)
    if l < size and arr[l] > arr[max_index]:
        max_index = l

    r = _right_child(i)
    if r < size and arr[r] > arr[max_index]:
        max_index = r

    if max_index != i:
        arr[max_index], arr[i] = arr[i], arr[max_index]
        _sift_down(arr, max_index, size)


class Heap:
    def __init__(self, arr=None):
        if arr is None:
            arr = []

        self.heap = arr
        self.size = len(arr)
        self.__heapify(self.heap)

    @staticmethod
    def __heapify(arr):
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            _sift_down(arr, i, n)

    def insert(self, key):
        if self.size == len(self.heap):
            self.heap.append(key)
        else:
            self.heap[self.size] = key

        _sift_up(self.heap, self.size)
        self.size += 1

    def extract_max(self):
        if self.size == 0:
            return 'No elements'

        max_val = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        _sift_down(self.heap, 0, self.size)

        return max_val

    def get_max(self):
        return self.heap[0]

    def remove(self, key):
        try:
            i = self.heap.index(key)
        except ValueError:
            return 'Key not found'

        self.heap[i] = float("inf")
        _sift_up(self.heap, i)
        self.extract_max()

    def change_priority(self, key, priority):
        try:
            i = self.heap.index(key)
        except ValueError:
            return 'Key not found'

        old_priority = self.heap[i]
        self.heap[i] = priority

        if old_priority < priority:
            _sift_up(self.heap, i)
        else:
            _sift_down(self.heap, i, self.size)

    def print_heap(self):
        return self.heap

    @classmethod
    def heap_sort(cls, arr):
        cls.__heapify(arr)
        size = len(arr)

        for i in range(len(arr) - 1):
            arr[0], arr[size-1] = arr[size-1], arr[0]
            size -= 1
            _sift_down(arr, 0, size)

        return arr


def main():
    arr = [13, 4, 8, 10, 2, 0, 15, 13, 12, 14]
    print(Heap.heap_sort(arr))


if __name__ == '__main__':
    main()