# python 3

def reverse(arr, i, j):
    while i < j:
        arr[i], arr[j] = arr[j], arr[i]
        i += 1
        j -= 1


def reverse_in_k(arr, n, k):
    iteration = 0
    while iteration < n:
        i = iteration * k
        j = min(i + k - 1, n - 1)

        reverse(arr, i, j)

        if (iteration * k) + k - 1 >= n:
            break

        iteration += 1

    return arr


def reverse_in_k_2(arr, n, k):
    i = 0
    while i < n:
        j = i + k - 1 if i + k < n else n - 1
        reverse(arr, i, j)
        i += k

    return arr


def main():
    arr = list(map(int, input().split()))
    k = int(input())
    reverse_in_k(arr, len(arr), k)
    print(arr)


if __name__ == '__main__':
    main()
