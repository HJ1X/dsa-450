# python 3

from double_linked_list_class import DoubleLinkedList


def rotate_by_1(head, tail):
    tail.next = head
    head.prev = tail

    new_head = head.next
    new_tail = head

    head.next.prev = None
    tail.next.next = None

    return new_head, new_tail


def rotate_dll(head, tail, k):
    for i in range(k):
        head, tail = rotate_by_1(head, tail)

    return head


def rotate_dll_efficient(head, k):
    tail = None
    curr = head
    while curr is not None:
        tail = curr
        curr = curr.next

    curr = head
    for i in range(k-1):
        curr = curr.next

    new_head = curr.next
    new_head.prev = None
    curr.next = None
    tail.next = head
    head.prev = tail

    return new_head


def reverse_dll_in_k(head, k):
    if head.next is None:
        return head

    curr = head
    temp = None
    count = 0

    while curr is not None and count < k:
        temp = curr.prev
        curr.prev = curr.next
        curr.next = temp
        curr = curr.prev
        count += 1

    if curr:
        curr.prev.prev = None
        curr.prev = None
        head.next = reverse_dll_in_k(curr, k)
        head.next.prev = head

    return temp.prev


def main():
    arr = list(map(int, input().split()))
    dll = DoubleLinkedList.create_dll(arr)
    print(dll)

    # head = rotate_dll(dll.head, dll.tail, 3)
    # head = rotate_dll_efficient(dll.head, 3)
    head = reverse_dll_in_k(dll.head, 3)
    dll.print_list(head)


if __name__ == '__main__':
    main()
