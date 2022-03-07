# python
from linked_list.linked_list_basics import LinkedList


def is_palindrome(head):
    if not head.next:  # only 1 node
        return True

    if not head.next.next:  # two nodes
        if head.data == head.next.data:
            return True
        else:
            return False

    slow = head.next
    fast = head.next.next
    mid = None
    terminating_node = None

    while True:
        if not fast.next:
            terminating_node = slow
            mid = slow.next
            break
        if not fast.next.next:
            terminating_node = slow.next
            mid = slow.next
            break
        slow = slow.next
        fast = fast.next.next

    # now reverse list from mid and then compare two it with original list till terminating node(not including)
    prev = None
    curr = mid
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr = nxt
    head_rev = prev

    # comparing two lists
    curr1 = head
    curr2 = head_rev
    while curr1 is not terminating_node:
        if curr1.data != curr2.data:
            return False
        curr1 = curr1.next
        curr2 = curr2.next
    return True


def main():
    arr = list(map(int, input().split()))
    linked_list = LinkedList.create_list(arr)
    print(is_palindrome(linked_list.head))


if __name__ == '__main__':
    main()

