# python 3

from collections import deque, OrderedDict
from linked_list.double_linked_list_basics import DoubleLinkedList


class LRUCacheDeque:
    def __init__(self, cap):
        self.capacity = cap
        self.cache = {}
        self.order = deque()

    def get(self, key):
        if key not in self.cache:
            return -1

        self.order.remove(key)
        self.order.append(key)
        return self.cache[key]

    def set(self, key, value):
        if key in self.cache:
            self.order.remove(key)

        elif len(self.cache) == self.capacity:
            key_to_remove = self.order.popleft()
            self.cache.pop(key_to_remove)

        self.cache[key] = value
        self.order.append(key)


class LRUCacheDLL:
    def __init__(self, cap):
        self.capacity = cap
        self.cache = {}
        self.order = DoubleLinkedList()

    def __repr__(self):
        repr_str = ''
        repr_str += f'cache: {self.cache}  order: {self.order}'
        return repr_str

    def get(self, key):
        if key not in self.cache:
            return -1

        key, value = self.order.erase_node(self.cache[key])
        node = self.order.push_back((key, value))
        self.cache[key] = node
        return node.data[1]

    def set(self, key, value):
        if key in self.cache:
            self.order.erase_node(self.cache[key])

        elif len(self.cache) == self.capacity:
            key_to_remove = self.order.pop_front()
            self.cache.pop(key_to_remove)

        node = self.order.push_back((key, value))
        self.cache[key] = node


class LRUCacheOrderedDict:
    def __init__(self, cap):
        self.capacity = cap
        self.cache = OrderedDict()

    def __repr__(self):
        repr_str = ''
        repr_str += f'cache: {self.cache}'
        return repr_str

    def get(self, key):
        if key not in self.cache:
            return -1

        self.cache.move_to_end(key)
        return self.cache[key]

    def set(self, key, value):
        if key in self.cache:
            self.cache.move_to_end(key)

        elif len(self.cache) == self.capacity:
            self.cache.popitem(last=False)

        self.cache[key] = value


def main():
    cap = int(input())
    data = input().split()
    cache = LRUCacheDLL(cap)

    i = 0
    while i < len(data):
        if data[i] == 'SET':
            cache.set(data[i+1], data[i+2])
            i += 3

        else:
            print(cache.get(data[i+1]))
            i += 2


if __name__ == '__main__':
    main()
