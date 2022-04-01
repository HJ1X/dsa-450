# python 3

from stacks_and_queues.stacks.stack_with_max_operations import StackWithMax


class QueueUsingStack:
    def __init__(self):
        self.__stack1 = StackWithMax()
        self.__stack2 = StackWithMax()

    def __repr__(self):
        repr_string = ''
        repr_string += f'Queue: {str(self.__stack1)[::-1]}{str(self.__stack2)}  Max: {self.max()}'
        return repr_string

    def enque(self, value):
        self.__stack1.push(value)

    def deque(self):
        if self.__stack2.is_empty():
            if self.__stack1.is_empty():
                raise IndexError('Could not deque from empty queue')

            while not self.__stack1.is_empty():
                val = self.__stack1.pop()
                self.__stack2.push(val)

        return self.__stack2.pop()

    def max(self):
        if not self.__stack1:
            return self.__stack2.max()
        elif not self.__stack2:
            return self.__stack1.max()
        else:
            return max(self.__stack1.max(), self.__stack2.max())


def main():
    queue = QueueUsingStack()
    queue.enque(1)
    queue.deque()
    queue.enque(2)
    queue.enque(3)
    queue.enque(4)
    print(queue.max())
    queue.enque(5)
    queue.deque()
    queue.deque()
    print(queue.max())


if __name__ == '__main__':
    main()
