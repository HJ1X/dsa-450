# Python 3

from linked_list.linked_list_basics import LinkedList, find_mid, Node
from linked_list.merge_two_sorted_linked_list import merge


def merge_sort(head):
    if not head.next:
        return head

    mid = find_mid(head)
    head2 = mid.next
    mid.next = None

    head1 = merge_sort(head)
    head2 = merge_sort(head2)
    head = merge(head1, head2)

    return head


def main():
    pass


if __name__ == '__main__':
    main()
