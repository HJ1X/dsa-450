# python 3
from linked_list.linked_list_basics import LinkedList, Node


def reverse_left_right_dummy_node(head, left, right):
    dummy_node = Node(-1)
    dummy_node.next = head

    curr = head
    prev = dummy_node

    for i in range(left - 1):
        prev = curr
        curr = curr.next

    left_prev = prev
    prev = None

    for i in range(left, right + 1):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    left_prev.next.next = curr
    left_prev.next = prev

    return dummy_node.next


def reverse_left_right(head, left, right):
    if left == right:
        return head

    curr = head
    prev = None

    for i in range(left - 1):
        prev = curr
        curr = curr.next

    left_node = curr

    for i in range(left, right):
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    if left_node.next:
        left_node.next.next = curr
    else:
        head = curr
    left_node.next = curr.next
    curr.next = prev

    return head


def main():
    arr = list(map(int, input().split()))
    left, right = map(int, input().split())
    llist = LinkedList.create_list(arr)
    head = reverse_left_right(llist.head, left, right)
    head.print_list()


if __name__ == '__main__':
    main()
