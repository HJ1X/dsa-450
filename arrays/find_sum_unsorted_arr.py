# Python

def find_sum(arr, n, x):
    s = set()
    for i in arr:
        if (x-i) in s:
            return True
        s.add(i)
    return False


def main():
    n, x = map(int, input().split())
    arr = list(map(int, input().split()))
    print(find_sum(arr, n, x))


if __name__ == '__main__':
    main()