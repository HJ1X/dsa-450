# Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __repr__(self):
        return f'Node({self.data})'

    def print_list(self):
        curr = self

        while curr:
            if not curr.next:
                print(curr.data)
                return
            else:
                print(curr.data, '-> ', end='')

            curr = curr.next


def create_loop(head, tail, loop_node):
    temp = head

    for i in range(loop_node):
        temp = temp.next

    tail.next = temp


def find_mid(head):
    slow = head
    fast = head

    while fast.next is not None and fast.next.next is not None:
        slow = slow.next
        fast = fast.next.next

    return slow


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __repr__(self):
        llist = ''
        curr = self.head
        while curr:
            if not curr.next:
                llist += str(curr.data)
                return llist
            else:
                llist += str(curr.data) + ' -> '
            curr = curr.next

    @classmethod
    def create_list(cls, arr):
        llist = cls()
        for data in arr:
            llist.push_back(data)

        return llist

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
            print(llist)
        else:
            x = 0


if __name__ == '__main__':
    main()
