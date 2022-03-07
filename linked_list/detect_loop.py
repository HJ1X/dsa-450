# Python 3

from linked_list.linked_list_basics import LinkedList, create_loop


def find_loop(head):
    if head.next is None or head.next.next is None:
        return False
    fast = head.next.next
    slow = head.next

    while fast != slow:
        if fast.next is None or fast.next.next is None:
            return False
        fast = fast.next.next
        slow = slow.next

    return True


def main():
    arr = list(map(int, input().split()))
    linked_list = LinkedList.create_list(arr)
    create_loop(linked_list.head, linked_list.tail, 2)
    print(find_loop(linked_list.head))


if __name__ == '__main__':
    main()
