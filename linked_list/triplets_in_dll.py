# python 3
from double_linked_list_class import DoubleLinkedList


def count_triplets_dll_hash_map(head, x):
    hash_map = {}
    curr = head

    while curr is not None:
        hash_map[curr.data] = curr
        curr = curr.next

    count = 0
    i = head
    while i is not None:
        j = i.next
        while j is not None:
            curr_sum = i.data + j.data
            target = x - curr_sum
            if target in hash_map and hash_map[target] is not i and hash_map[target] is not j:
                count += 1
            j = j.next
        i = i.next

    return count // 3


def count_triplets_dll_two_pointer(head, tail, x):
    count = 0
    i = head
    while i.next is not None:
        j = i.next
        k = tail
        target = x - i.data

        while j is not k:
            if j.data + k.data == target:
                count += 1
                break

            elif j.data + k.data > target:
                k = k.prev
            else:
                j = j.next

        i = i.next
    return count


def main():
    dll = DoubleLinkedList()
    dll.push_back(1)
    dll.push_back(2)
    dll.push_back(4)
    dll.push_back(5)
    dll.push_back(6)
    dll.push_back(8)
    dll.push_back(9)
    x = 17
    # print(count_triplets_dll_hash_map(dll.head, x))
    print(count_triplets_dll_two_pointer(dll.head, dll.tail, x))


if __name__ == '__main__':
    main()
