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

    # def find_mid(self, head, tail):
    #     slow = head
    #     fast = head
    #     while fast is not tail and fast.next is not tail:
    #         slow = slow.next
    #         fast = fast.next.next
    #     return slow

    def find_mid(self, head):
        slow = head
        fast = head
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next

        return slow

    def merge(self, head1, head2):
        # curr1 = head1
        # curr2 = head2
        #
        # merge_arr = []
        # while curr1 is not mid.next and curr2 is not tail.next:
        #     if curr1.data < curr2.data:
        #         merge_arr.append(curr1.data)
        #         curr1 = curr1.next
        #     else:
        #         merge_arr.append(curr2.data)
        #         curr2 = curr2.next
        # while curr1 != mid:
        #     merge_arr.append(curr1.data)
        # while curr2 != tail:
        #     merge_arr.append(curr2.data)

        # for i in merge_arr:
        #     head1.data = i
        #     head1 = head1.next

        res = None
        temp = None

        if head1.data < head2.data:
            res = head1
            temp = head1
            head1 = head1.next

        else:
            res = head2
            temp = head2
            head2 = head2.next

        while head1 and head2:
            if head1.data < head2.data:
                temp.next = head1
                head1 = head1.next
            else:
                temp.next = head2
                head2 = head2.next
            temp = temp.next

        if head1:
            temp.next = head1

        if head2:
            temp.next = head2

        return res

    def merge_sort(self, head):
        if not head.next:
            return head

        mid = self.find_mid(head)
        head2 = mid.next
        mid.next = None

        head1 = self.merge_sort(head)
        head2 = self.merge_sort(head2)

        head = self.merge(head1, head2)
        return head

    def segg_odd_even(self, head):

        dummy_even = Node(-1)
        dummy_odd = Node(-1)

        tail_odd, tail_even, curr = dummy_odd, dummy_even, head

        while curr:
            if curr.data % 2 == 0:
                tail_even.next = curr
                tail_even = tail_even.next

            else:
                tail_odd.next = curr
                tail_odd = tail_odd.next

            curr = curr.next

        tail_odd.next = dummy_even.next
        tail_even.next = None
        return dummy_odd.next


def main():
    llist = LinkedList()
    llist.push_back(3)
    llist.push_back(5)
    llist.push_back(2)
    llist.push_back(4)
    llist.push_back(1)
    llist.print_list()
    print()
    # llist.head = llist.merge_sort(llist.head)
    # llist.print_list()
    llist.segg_odd_even(llist.head)
    llist.print_list()


if __name__ == '__main__':
    main()
