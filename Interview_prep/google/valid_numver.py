# python 3

def is_valid(num):
    decimal_flag = 0
    if num[0] == '+' or num[0] == '-':
        num = num[1:]

    for i in range(len(num)):
        if '0' <= num[i] <= '9':
            continue

        elif num[i] == '.' and not decimal_flag:
            decimal_flag = 1
            if i == len(num) - 1:
                return False

        else:
            return False

    return True


def main():
    num = input()
    print(is_valid(num))


if __name__ == '__main__':
    main()