# python 3

def interleave(queue):
    n = len(queue)
    stack = []

    for i in range(n//2):
        stack.append(queue.pop(0))

    while stack:
        queue.append(stack.pop())

    for i in range(n//2):
        queue.append(queue.pop(0))

    for i in range(n//2):
        stack.append(queue.pop(0))

    while stack:
        queue.append(stack.pop())
        queue.append(queue.pop(0))

    return queue


def main():
    arr = list(map(int, input().split()))
    print(interleave(arr))


if __name__ == '__main__':
    main()
