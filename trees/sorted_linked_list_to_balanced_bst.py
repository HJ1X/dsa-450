# python 3
from linked_list.linked_list_basics import LinkedList
from trees.tree_basics import Node


def count_nodes(head):
    curr = head
    count = 0

    while curr:
        count += 1
        curr = curr.next

    return count


def create_tree(curr, n):
    if n <= 0:
        return

    left = create_tree(curr, n // 2)
    root = Node(curr[0].data)
    curr[0] = curr[0].next
    right = create_tree(curr, n - n // 2 - 1)

    root.left = left
    root.right = right
    return root


def list_to_arr(head):
    arr = []
    curr = head
    while curr:
        arr.append(curr.data)
        curr = curr.next

    return arr


def arr_to_bst(arr):
    if not arr:
        return

    mid = len(arr) // 2
    left = arr_to_bst(arr[:mid])

    root = Node(arr[mid])
    root.left = left

    root.right = arr_to_bst(arr[mid + 1:])
    return root


def sorted_list_to_bst(head):
    # n = count_nodes(head)
    # curr = [head]
    # root = create_tree(curr, n)
    # return root

    arr = list_to_arr(head)
    root = arr_to_bst(arr)
    return root


def main():
    arr = list(map(int, input().split()))
    head = LinkedList.create_list(arr)
    root = sorted_list_to_bst(head)
    root.print_tree()


if __name__ == '__main__':
    main()
