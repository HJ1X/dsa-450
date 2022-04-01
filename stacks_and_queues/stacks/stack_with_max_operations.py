# python 3

class StackWithMax:
    def __init__(self):
        self.__stack = []
        self.__max = []

    def __str__(self):
        string = ''
        for i in range(len(self.__stack)):
            string += str(self.__stack[i]) + ' '

        return string

    def __repr__(self):
        repr_string = ''
        repr_string += f'Stack: {self.__stack}  Max: {self.max()}'
        return repr_string

    def __len__(self):
        return len(self.__stack)
    #
    # def __getitem__(self, key):
    #     if 0 <= key < len(self.__stack):
    #         return self.__stack[key]
    #     else:
    #         raise IndexError
    #
    # def __reversed__(self):
    #     for i in range(len(self.__stack)-1, -1, -1):
    #         yield self.__stack[i]

    def push(self, data):
        self.__stack.append(data)
        if not self.__max or data >= self.__max[-1]:
            self.__max.append(data)

    def pop(self):
        if not self.__stack:
            return 'Stack Empty'

        data = self.__stack.pop()
        if self.__max[-1] == data:
            self.__max.pop()

        return data

    def max(self):
        if not self.__stack:
            return 'Stack Empty'

        return self.__max[-1]

    def is_empty(self):
        return False if len(self.__stack) else True


def main():
    pass


if __name__ == '__main__':
    main()
