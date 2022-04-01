# python 3

def reverse_first_k(queue, k):
    n = len(queue)
    stack = []

    for i in range(k):
        stack.append(queue.pop(0))

    while stack:
        queue.append(stack.pop())

    for i in range(n - k):
        queue.append(queue.pop(0))

    return queue


def main():
    pass


if __name__ == '__main__':
    main()
