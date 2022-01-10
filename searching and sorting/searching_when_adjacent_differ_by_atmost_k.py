# python 3

def search(n, arr, k, x):
    i = 0
    while i < n:
        if arr[i] == x:
            return i

        diff = abs(arr[i] - x)
        i += max(1, diff // k)

    return -1


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    k = int(input())
    x = int(input())
    print(search(n, arr, k, x))


if __name__ == '__main__':
    main()