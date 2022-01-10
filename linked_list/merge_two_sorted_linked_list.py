# python 3


def sorted_merge(head1, head2):
    # code here

    temp = None
    res = None
    if head1.data < head2.data:
        temp = head1
        res = head1
        head1 = head1.next
    else:
        temp = head2
        res = head2
        head2 = head2.next

    while head1 and head2:
        if head1.data < head2.data:
            temp.next = head1
            head1 = head1.next
        else:
            temp.next = head2
            head2 = head2.next

    if head1:
        temp.next = head1

    if head2:
        temp.next = head2

    return res


def main():
    head1 = None # should be node
    head2 = None # should be node
    print(sorted_merge(head1, head2))


if __name__ == '__main__':
    main()
