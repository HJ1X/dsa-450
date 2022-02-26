# Python 3

class Node:
    def __init__(self, key):
        self.data = key
        self.next = None
        self.arb = None


class LinkedListWithArb:
    def __init__(self):
        self.head = None
        self.tail = None

    def push_back(self, data):
        new_node = Node(data)
        if not self.tail:
            self.tail, self.head = new_node, new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def find_node(self, key):
        curr = self.head
        while curr:
            if curr.data == key:
                return curr
            curr = curr.next

        raise KeyError('Node with given key not found')

    @classmethod
    def add_nodes(cls, arr, pairs):
        llist = cls()
        for data in arr:
            llist.push_back(data)

        for pair in pairs:
            node_from = llist.find_node(pair[0])
            node_to = llist.find_node(pair[1])
            node_from.arb = node_to

        return llist


def copy_list(head):
    # cloning list with just next pointers
    new_head = Node(-1)

    curr = head
    curr_new = new_head

    while curr:
        new_node = Node(curr.data)
        curr_new.next = new_node
        curr = curr.next
        curr_new = curr_new.next

    # Removing dummy head node -1
    new_head = new_head.next

    # Changing links to get arb pointers
    curr = head
    curr_new = new_head

    while curr:
        temp = curr.next
        curr.next = curr_new
        curr_new.arb = curr
        curr = temp
        curr_new = curr_new.next

    # Finally, changing arb pointers to actual nodes of new_list
    curr = new_head
    while curr:
        if curr.arb.arb:
            curr.arb = curr.arb.arb.next
        else:
            curr.arb = None
        curr = curr.next

    return new_head


def copy_list_best(head):
    # Inserting new nodes in between original list
    curr = head
    while curr is not None:
        new_node = Node(curr.data)
        new_node.next = curr.next
        curr.next = new_node
        curr = curr.next.next

    # Setting arb pointers of new_nodes inserted between original list
    curr = head
    while curr is not None:
        if curr.arb:
            curr.next.arb = curr.arb.next
        else:
            curr.next.arb = None
        curr = curr.next.next

    # Separating both the lists
    new_head = Node(-1)
    curr_new = new_head
    curr = head
    while curr:
        curr_new.next = curr.next
        curr.next = curr.next.next
        curr = curr.next
        curr_new = curr_new.next
    return new_head.next


def main():
    arr = list(map(int, input().split()))
    pairs = []
    while True:
        val = input()
        if val == '':
            break
        pairs.append(list(map(int, val.split())))

    llist = LinkedListWithArb.add_nodes(arr, pairs)
    head = copy_list(llist.head)
    curr = head
    while curr:
        print(curr.data, curr.arb.data if curr.arb else None)
        curr = curr.next


if __name__ == '__main__':
    main()