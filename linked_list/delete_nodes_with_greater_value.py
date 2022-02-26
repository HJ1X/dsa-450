# python 3

from linked_list.reverse_linked_list import LinkedList
from linked_list.reverse_linked_list import Node


# ------------------------------------------- Wrong interpretation of problem --------------------------------------- #
def remove_greater(head):
    new_head = Node(-1)

    curr = head
    curr_new = new_head

    while curr.next:
        if curr.next.data <= curr.data:
            curr_new.next = curr
            curr_new = curr_new.next
        curr = curr.next

    curr_new.next = curr
    return new_head.next
# ------------------------------------------------------------------------------------------------------------------- #


def reverse_list(head):
    curr = head
    prev = None

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


def remove_greater_from_rights(head):
    head = reverse_list(head)

    max_till_now = head.data
    curr = head

    while curr.next:
        # Delete node if less than max_till_now
        if curr.next.data < max_till_now:
            curr.next = curr.next.next

        else:
            max_till_now = curr.next.data
            curr = curr.next

    return reverse_list(head)


def remove_greater_from_right_stack(head):
    stack = []
    curr = head

    while curr is not None:
        stack.append(curr)
        curr = curr.next

    next_node = stack.pop()
    max_till_now = next_node.data

    while stack:
        curr = stack.pop()
        if curr.data >= max_till_now:
            max_till_now = curr.data
            curr.next = next_node
            next_node = curr

    return next_node


def remove_greater_from_rights_recursive(head):
    if head.next is None:
        return head

    next_node = remove_greater_from_rights_recursive(head.next)

    if next_node.data > head.data:
        return next_node
    else:
        head.next = next_node
        return head


def main():
    arr = list(map(int, input().split()))
    head = LinkedList.create_list(arr)
    head = remove_greater_from_right_stack(head)
    LinkedList.print_list(head)


if __name__ == '__main__':
    main()
