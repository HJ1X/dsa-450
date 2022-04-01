# python 3
from collections import deque


def check_mirror_tree_hash_map(e, nodes1, nodes2):
    hash_map = {}
    i = 0
    while i < 2 * e:
        u = nodes1[i]
        v = nodes1[i + 1]

        if u in hash_map:
            hash_map[u].append(v)
        else:
            hash_map[u] = [v]

        i += 2

    i = 0
    while i < 2 * e:
        u = nodes2[i]
        v = nodes2[i + 1]

        if u in hash_map:
            v_1 = hash_map[u].pop()
            if v_1 != v:
                return 0
        else:
            return 0

        i += 2

    return 1


# The idea is to do a preorder traversal of tree1 and store in stack
# Then, do a postorder traversal of tree2 and store in queue
# Now, remove elements from stacks and queues and check, if not equal return 'NOT MIRROR'

def preorder_stack(root, stack):
    if root is None:
        return

    stack.append(root.data)
    preorder_stack(root.left, stack)
    preorder_stack(root.right, stack)


def postorder_queue(root, queue):
    if root is None:
        return

    postorder_queue(root.left, queue)
    postorder_queue(root.right, queue)
    queue.appendleft(root.data)


def check_mirror_stack_queue(root1, root2):
    stack = []
    preorder_stack(root1, stack)

    queue = deque()
    postorder_queue(root2, queue)

    for i in range(len(stack)):
        if stack.pop() != queue.pop():
            return False

    return True


def main():
    pass


if __name__ == '__main__':
    main()
