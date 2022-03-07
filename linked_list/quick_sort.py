# python 3
from linked_list.linked_list_basics import Node


def partition(head, x):
    left_head = Node(-1)
    mid_head = Node(-1)
    right_head = Node(-1)

    curr = head
    curr_left = left_head
    curr_mid = mid_head
    curr_right = right_head

    while curr:
        if curr.data < x:
            curr_left.next = curr
            curr_left = curr_left.next

        elif curr.data == x:
            curr_mid.next = curr
            curr_mid = curr_mid.next

        else:
            curr_right.next = curr
            curr_right = curr_right.next

        curr = curr.next

    curr_right.next = None
    curr_mid.next = right_head.next
    curr_left.next = mid_head.next
    return left_head.next


def main():
    pass


if __name__ == '__main__':
    main()
