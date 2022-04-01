# python 3
from linked_list.linked_list_basics import LinkedList


def swap_kth_node(head, n, k):
    if k > n:
        return head

    if k > n // 2:   # Keeping k's value in the first half
        k = n - k + 1

    ptr1_prev = None
    ptr1 = head     # kth node
    ptr2_prev = None
    ptr2 = head     # (n-k)th node

    for i in range(k-1):
        ptr1_prev = ptr1
        ptr1 = ptr1.next

    for i in range(n-k):
        ptr2_prev = ptr2
        ptr2 = ptr2.next

    # Pointing prev nodes to new ptr nodes
    if ptr1_prev:
        ptr1_prev.next = ptr2
    else:   # If k is 1, make (n-k)th node head
        head = ptr2

    ptr2_prev.next = ptr1

    # Swapping next pointers of ptr nodes
    ptr1.next, ptr2.next = ptr2.next, ptr1.next

    return head


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    llist = LinkedList.create_list(arr)
    head = swap_kth_node(llist.head, n, k)
    head.print_list()


if __name__ == '__main__':
    main()
