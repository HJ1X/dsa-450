# python 3

from linked_list.double_linked_list_basics import DoubleLinkedList


class StackWithMid:
    def __init__(self):
        self.__stack = DoubleLinkedList()
        self.__mid = self.__stack.head
        self.__change_mid = True

    def __repr__(self):
        repr_str = self.__stack.__repr__()
        repr_str += f'\tMid : {self.__mid.data if self.__mid else None}'
        return repr_str

    def push(self, data):
        self.__stack.push_back(data)
        if self.__mid is None:
            self.__mid = self.__stack.head
        elif self.__change_mid:
            self.__mid = self.__mid.next

        self.__change_mid = not self.__change_mid

    def pop(self):
        if self.__stack.empty():
            return 'Empty stack!!'

        data = self.__stack.pop_back()
        if not self.__change_mid:
            self.__mid = self.__mid.prev

        self.__change_mid = not self.__change_mid
        return data

    def top_mid(self):
        return self.__mid.data

    def pop_mid(self):
        if self.__stack.empty():
            return 'Empty stack!!'

        if not self.__change_mid:
            self.__mid = self.__mid.prev

        self.__stack.erase_node(self.__mid.next)
        self.__change_mid = not self.__change_mid


def main():
    stack = StackWithMid()
    stack.push(1)
    print(stack)
    stack.push(2)
    print(stack)
    stack.push(3)
    print(stack)
    stack.push(4)
    print(stack)
    stack.push(5)
    print(stack)
    stack.pop()
    print(stack)
    stack.pop()
    print(stack)
    stack.pop_mid()
    print(stack)


if __name__ == '__main__':
    main()
