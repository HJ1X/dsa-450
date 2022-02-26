# python 3

def merge(head1, head2):
    dummy_head = Node(-1)
    dummy_tail = dummy_head

    while head1 and head2:
        if head1.data < head2.data:
            dummy_tail.next = head1
            head1 = head1.next
        else:
            dummy_tail.next = head2
            head2 = head2.next
        dummy_tail = dummy_tail.next

    if head1:
        dummy_tail.next = head1

    if head2:
        dummy_tail.next = head2

    head = dummy_head.next
    return head


def merge_k_lists_divide_and_conquer(arr, k):
    last = k - 1

    # Until all the lists have been sorted
    while last != 0:
        i = 0
        j = last

        # Merging two lists at corresponding far ends
        while i < j:
            arr[i] = merge(arr[i], arr[j])
            i += 1
            j -= 1

        last = j
    return arr[0]


def merge_k_lists(arr, k):
    for i in range(k - 1):
        arr[0] = merge(arr[0], arr[i + 1])

    return arr[0]


def main():
    pass


if __name__ == '__main__':
    main()
