# python 3

from linked_list.linked_list_basics import Node
from linked_list.linked_list_basics import LinkedList


def divide(head):
    even_head = Node(-1)
    odd_head = Node(-1)

    curr_even, curr_odd = even_head, odd_head
    curr = head

    while curr:
        if curr.data % 2 == 0:
            curr_even.next = curr
            curr_even = curr_even.next
        else:
            curr_odd.next = curr
            curr_odd = curr_odd.next

        curr = curr.next

    curr_odd.next = None
    curr_even.next = odd_head.next
    return even_head.next


def main():
    arr = list(map(int, input().split()))
    head = LinkedList.create_list(arr)
    head = divide(head)
    head.print_list()


if __name__ == '__main__':
    main()
