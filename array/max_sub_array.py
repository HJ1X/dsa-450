# python 3

def find_max_subarray(arr):
    n = len(arr)

    max_sum = 0
    max_i, max_j = 0, n

    curr_sum = 0
    curr_i = 0

    for i in range(n):
        if arr[i] < 0:
            curr_i = i + 1
            curr_sum = 0
        else:
            curr_sum += arr[i]

        if curr_sum >= max_sum:
            max_sum = curr_sum
            max_i = curr_i
            max_j = i

    return arr[max_i: max_j + 1]


def main():
    arr = list(map(int, input().split()))
    print(find_max_subarray(arr))


if __name__ == '__main__':
    main()
