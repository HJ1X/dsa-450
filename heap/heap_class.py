# python 3
import random


def parent(i):
    return (i-1) // 2


def left_child(i):
    return (2*i) + 1


def right_child(i):
    return (2*i) + 2


def sift_up(arr, i):
    while i > 0 and arr[parent(i)] < arr[i]:
        arr[parent(i)], arr[i] = arr[i], arr[parent(i)]
        i = parent(i)


def sift_down(arr, i, size):
    while i < size:
        max_index = i
        l = left_child(i)
        if l < size and arr[l] > arr[max_index]:
            max_index = l
        r = right_child(i)
        if r < size and arr[r] > arr[max_index]:
            max_index = r
        if max_index != i:
            arr[max_index], arr[i] = arr[i], arr[max_index]
            i = max_index
        else:
            return


class Heap:
    def __init__(self, max_size):
        self.max_size = max_size
        self.heap = [None] * max_size
        self.size = 0

    def __sift_up(self, i):
        while i > 0 and self.heap[parent(i)] < self.heap[i]:
            self.heap[parent(i)], self.heap[i] = self.heap[i], self.heap[parent(i)]
            i = parent(i)

    def __sift_down(self, i):
        while i >= 0:
            max_index = i
            l = left_child(i)
            if l < self.size and self.heap[l] > self.heap[max_index]:
                max_index = l

            r = right_child(i)
            if r < self.size and self.heap[r] > self.heap[max_index]:
                max_index = r

            if max_index != i:
                self.heap[max_index], self.heap[i] = self.heap[i], self.heap[max_index]
                i = max_index
            else:
                return

    def insert(self, p):
        if self.size == self.max_size:
            return 'Heap Full'

        self.size += 1
        self.heap[self.size - 1] = p
        self.__sift_up(self.size - 1)

    def extract_max(self):
        if self.size == 0:
            return 'No elements'
        max_val = self.heap[0]
        self.heap[0] = self.heap[self.size - 1]
        self.size -= 1
        self.__sift_down(0)

        return max_val

    def find_max(self):
        return self.heap[0]

    def remove(self, i):
        self.heap[i - 1] = float("inf")
        self.__sift_up(i - 1)
        self.extract_max()

    def change_priority(self, i, p):
        old_priority = self.heap[i-1]
        self.heap[i-1] = p

        if old_priority < p:
            self.__sift_up(i-1)
        else:
            self.__sift_down(i-1)

    def print_heap(self):
        return self.heap

    @staticmethod
    def build_heap(arr):
        for i in range((len(arr) // 2) - 1, -1, -1):
            sift_down(arr, i, len(arr))
        return arr


def heap_sort(arr):
    # h = Heap(10)
    # for i in arr:
    #     h.insert(i)
    # for i in reversed(range(len(arr))):
    #     arr[i] = h.extract_max()

    size = len(arr)
    arr = Heap.build_heap(arr)
    print(arr)
    for i in range(len(arr) - 1):
        arr[0], arr[size-1] = arr[size-1], arr[0]
        size -= 1
        sift_down(arr, 0, size)
    return arr


def main():
    # h = Heap(10)
    # print(h.print_heap())
    # print(h.extract_max())
    # h.insert(12)
    # h.insert(15)
    # h.insert(9)
    # h.insert(random.randint(1,20))
    # h.insert(random.randint(1,20))
    # h.insert(random.randint(1,20))
    # h.insert(random.randint(1,20))
    # h.insert(random.randint(1,20))
    # h.insert(random.randint(1,20))
    # print(h.print_heap())
    # print(h.extract_max())
    # print(h.extract_max())
    # print(h.find_max())
    # print(h.extract_max())
    # h.insert(19)
    # h.insert(13)
    # h.change_priority(2, 20)
    # h.print_heap()

    arr = [13, 4, 8, 10, 2, 0, 15, 13, 12, 14]
    print(heap_sort(arr))

if __name__ == '__main__':
    main()