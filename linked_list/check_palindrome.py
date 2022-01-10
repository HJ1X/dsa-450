# python

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
        while curr:
            print(curr.data, '-> ', end='')
            curr = curr.next

    def reverse(self):
        prev = None
        curr = self.head
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        self.head = prev

    def is_palindrome(self, head):
        if not head.next:  # only 1 node
            return True

        if not head.next.next:  # two nodes
            if head.data == head.next.data:
                return True
            else:
                return False

        slow = head.next
        fast = head.next.next
        mid = None
        terminating_node = None

        while True:
            if not fast.next:
                terminating_node = slow
                mid = slow.next
                break

            if not fast.next.next:
                terminating_node = slow.next
                mid = slow.next
                break

            slow = slow.next
            fast = fast.next.next

        # now reverse list from mid and then compare two it with original list till terminating node(not including)

        prev = None
        curr = mid

        while curr:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next

        head_rev = prev

        # comparing two lists

        curr1 = head
        curr2 = head_rev

        while curr1 is not terminating_node:
            if curr1.data != curr2.data:
                return False
            curr1 = curr1.next
            curr2 = curr2.next

        return True


def main():
    arr = list(map(int, input().split()))
    linked_list = LinkedList()

    for i in range(len(arr)):
        linked_list.push_back(arr[i])

    linked_list.print_list()
    print(linked_list.is_palindrome(linked_list.head))
    linked_list.print_list()


if __name__ == '__main__':
    main()

