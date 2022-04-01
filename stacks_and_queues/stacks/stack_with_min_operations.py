# python 3

class StackWithMin:
    def __init__(self):
        self.__stack = []
        self.__min = []

    def push(self, data):
        self.__stack.append(data)
        if not self.__min or data <= self.__min[-1]:
            self.__min.append(data)

    def pop(self):
        if not self.__stack:
            return 'Stack Empty'

        data = self.__stack.pop()
        if self.__min[-1] == data:
            self.__min.pop()

        return data

    def min(self):
        if not self.__stack:
            return 'Stack Empty'

        return self.__min[-1]


def main():
    pass


if __name__ == '__main__':
    main()
