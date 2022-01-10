# python 3

def print_paren_combinations(n, string, left, right):
    if right == n:
        print(string)

    if left < n:
        print_paren_combinations(n, string + '(', left + 1, right)

    if right < left:
        print_paren_combinations(n, string + ')', left, right + 1)


def main():
    n = int(input())
    print_paren_combinations(n, '', 0, 0)


if __name__ == '__main__':
    main()