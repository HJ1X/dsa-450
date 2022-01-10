# Python 3

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

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

    def print_list(self):
        curr = self.head
        if not curr:
            print('Empty list')
        count = 0
        while curr and count < 12:
            print(curr.data)
            curr = curr.next
            count += 1

    def create_loop(self, x):
        if x == 0:
            return

        temp = self.head
        for i in range(1, x):
            temp = temp.next

        self.tail.next = temp


def delete_loop(head):
    if head.next is None or head.next.next is None:
        return

    fast = head.next.next
    slow = head.next

    while fast != slow:
        if fast.next is None or fast.next.next is None:
            return
        fast = fast.next.next
        slow = slow.next

    fast = head

    while fast != slow:
        fast = fast.next
        slow = slow.next

    temp = fast
    while temp.next != fast:
        temp = temp.next

    temp.next = None


def main():
    linked_list = LinkedList()
    linked_list.push_back(1)
    linked_list.push_back(8)
    linked_list.push_back(3)
    linked_list.push_back(4)

    linked_list.create_loop(2)
    linked_list.print_list()
    delete_loop(linked_list.head)
    print('After: \n')
    linked_list.print_list()


if __name__ == '__main__':
    main()
