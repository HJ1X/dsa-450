# python 3

from linked_list.linked_list_basics import LinkedList


def reverse(head):
    prev = None
    curr = head

    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt

    return prev


def reverse_util(curr, prev):
    if not curr:
        return prev

    nxt = curr.next
    curr.next = prev

    return reverse_util(nxt, curr)


def reverse_recursive(head):
    if not head:
        return
    return reverse_util(head, None)


def main():
    arr = list(map(int, input().split()))
    llist = LinkedList.create_list(arr)
    head = reverse_recursive(llist.head)
    head.print_list()


if __name__ == '__main__':
    main()
