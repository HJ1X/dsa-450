# Python 3

from linked_list.linked_list_basics import LinkedList, create_loop


def delete_loop(head):
    if head.next is None or head.next.next is None:
        return

    fast = head.next.next
    slow = head.next

    while fast != slow:
        if fast.next is None or fast.next.next is None:
            return
        fast = fast.next.next
        slow = slow.next

    fast = head

    while fast != slow:
        fast = fast.next
        slow = slow.next

    temp = fast
    while temp.next != fast:
        temp = temp.next

    temp.next = None


def main():
    arr = list(map(int, input().split()))
    linked_list = LinkedList.create_list(arr)
    create_loop(linked_list.head, linked_list.tail, 2)
    delete_loop(linked_list.head)
    print(linked_list)


if __name__ == '__main__':
    main()
