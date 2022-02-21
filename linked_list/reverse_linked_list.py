# Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def push_front(head, data):
    new_node = Node(data)
    new_node.next = head
    return new_node


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    @staticmethod
    def create_list(arr):
        head = None
        for data in reversed(arr):
            head = push_front(head, data)

        return head

    def push(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
        if not self.tail:
            self.tail = new_node

    def push_back(self, data):
        new_node = Node(data)
        if not self.tail:
            self.head = new_node
            self.tail = new_node
            return
        self.tail.next = new_node
        self.tail = new_node

    def pop(self):
        if not self.head:
            return 'List empty'
        temp = self.head
        val = temp.data
        if self.tail == self.head:
            self.tail = None
            self.head = None
            del temp
            return val
        self.head = temp.next
        del temp
        return val

    def pop_back(self):
        if not self.head:
            return 'List empty'
        temp = self.head
        if self.head == self.tail:
            self.head = None
            self.tail = None
            val = temp.data
            del temp
            return val
        while temp.next.next:
            temp = temp.next
        self.tail = temp
        self.tail.next = None
        val = temp.next.data
        del temp.next
        return val

    @staticmethod
    def print_list(head=None):
        if not head:
            return 'No list given'

        curr = head
        if not curr:
            print('Empty list')
        while curr:
            print(curr.data, '-', end='', sep='')
            curr = curr.next
        print()

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def reverse_util(self, curr, prev):
        if not curr.next:
            self.head = curr
            curr.next = prev
            return
        next = curr.next
        curr.next = prev
        self.reverse_util(next, curr)

    def reverse_recursive(self):
        if not self.head:
            return
        self.reverse_util(self.head, None)

    def copy(self):
        new_list = LinkedList()
        curr = self.head
        while curr:
            new_list.push_back(curr.data)
            curr = curr.next

        return new_list


def main():
    llist = LinkedList()
    x = 1
    while x:
        y = int(input('Choose operation: '))
        if y == 1:
            data = int(input('Enter data: '))
            llist.push(data)
        elif y == 2:
            data = int(input('Enter data: '))
            llist.push_back(data)
        elif y == 3:
            data = llist.pop()
            print(data)
        elif y == 4:
            data = llist.pop_back()
            print(data)
        elif y == 5:
            llist.print_list()
        elif y == 6:
            llist.reverse()
        elif y == 7:
            llist.reverse_recursive()
        elif y == 8:
            new_list = llist.copy()
            llist.print_list()
            new_list.print_list()
        else:
            x = 0


if __name__ == '__main__':
    main()
