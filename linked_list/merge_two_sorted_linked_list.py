# python 3

from linked_list.linked_list_basics import Node


def merge(head1, head2):
    new_head = Node(-1)

    curr1 = head1
    curr2 = head2

    # if curr1.data < curr2.data:
    #     new_head = curr1
    #     curr1 = curr1.next

    # else:
    #     new_head = curr2
    #     curr2 = curr2.next

    curr_new = new_head

    while curr1 is not None and curr2 is not None:
        if curr1.data < curr2.data:
            curr_new.next = curr1
            curr1 = curr1.next

        else:
            curr_new.next = curr2
            curr2 = curr2.next

        curr_new = curr_new.next

    if curr1:
        curr_new.next = curr1
    else:
        curr_new.next = curr2

    return new_head.next


def main():
    pass


if __name__ == '__main__':
    main()
