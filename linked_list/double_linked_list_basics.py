# python 3
import random


class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

    def __str__(self):
        return f'data: {self.data}'


class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        dll = ''
        curr = self.head
        while curr:
            if curr.next is None:
                dll += str(curr.data)
                return dll
            dll += str(curr.data) + ' <-> '
            curr = curr.next

    def __repr__(self):
        return_str = ''
        return_str += 'LinkedList: ' + self.__str__() + '\n'
        return_str += 'Object Attributes: ' + '\n'
        return_str += '\t' + 'Head: ' + str(self.head.data) + '\n'
        return_str += '\t' + 'Tail: ' + str(self.tail.data) + '\n'
        return return_str

    @classmethod
    def create_dll(cls, arr):
        dll = cls()
        for ele in arr:
            dll.push_back(ele)
        return dll

    def push_front(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head     # new_node.prev is already None
            new_node.next.prev = new_node
            self.head = new_node

    def push_back(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def pop_front(self):
        if not self.head:
            return 'List Empty'

        val = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return val

    def pop_back(self):
        if not self.head:
            return 'List Empty'

        val = self.head.data
        if self.head == self.tail:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return val

    def top_front(self):
        return self.head.data

    def top_back(self):
        return self.tail.data

    def find(self, key):
        if not self.head:
            return 'List Empty'

        temp = self.head
        while temp.next is not None:
            if temp.data == key:
                return temp
            temp = temp.next

        return False

    def erase_key(self, key, all_occurrence=None):
        if not self.head:
            return 'List Empty'

        temp = self.head
        while temp is not None:
            if temp.data == key:
                if temp.prev is not None:
                    temp.prev.next = temp.next
                if temp.next is not None:
                    temp.next.prev = temp.prev
                if not all_occurrence:
                    return
            temp = temp.next

    def erase_node(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        return

    def empty(self):
        if not self.head:
            return True
        else:
            return False

    def add_after(self, node, data):
        if not node:
            return 'Wrong node'

        new_node = Node(data)

        new_node.next = node.next
        new_node.prev = node
        node.next = new_node
        if new_node.next is not None:
            new_node.next.prev = new_node
        if self.tail == node:
            self.tail = new_node

    def add_before(self, node, data):
        if not node:
            return 'Wrong node'

        new_node = Node(data)

        new_node.prev = node.prev
        new_node.next = node
        node.prev = new_node
        if new_node.prev is not None:
            new_node.prev.next = new_node
        if self.head is node:
            self.head = new_node

    @classmethod
    def print_list(cls, head):
        curr = head
        while curr is not None:
            if curr.next is None:
                print(curr.data)
                return
            print(curr.data, '<-> ', end='')
            curr = curr.next
        print()


def main():
    dll = DoubleLinkedList()
    dll.push_front(random.randint(1,20))
    dll.push_front(random.randint(1,20))
    dll.push_front(16)
    dll.push_front(random.randint(1,20))
    dll.push_front(random.randint(1,20))
    # dll.print_list()
    dll.push_back(14)
    # dll.print_list()
    dll.pop_back()
    # dll.print_list()
    dll.pop_front()
    # dll.print_list()
    node = dll.find(16)
    dll.add_after(node, 90)
    # dll.print_list()
    dll.add_before(node, 69)
    # dll.print_list()
    dll.erase_key(18, all_occurrence=True)
    # dll.print_list()
    dll.push_back(90)
    dll.push_back(90)
    dll.push_back(68)
    dll.push_back(90)
    # dll.print_list()
    dll.erase_key(90, all_occurrence=True)
    # dll.print_list()
    dll.erase_node(node)
    # dll.print_list()
    print(dll)
    print(repr(dll))


if __name__ == '__main__':
    main()
