# python 3


def reverse(arr, left, right):
    while left <= right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1


def find_next_permutation(arr):
    n = len(arr)

    # Finding the first decreasing element
    i = n - 1
    decreasing_index = -1
    while i > 0:
        if arr[i-1] < arr[i]:
            decreasing_index = i - 1
            break
        i -= 1

    # if no decreasing index is found than it means, it was last permutation,
    # so we should return first permutation by reversing
    if decreasing_index == -1:
        arr.reverse()
        return

    else:
        i = n - 1
        bigger_than_decreasing_index = None
        while arr[i] <= arr[decreasing_index]:
            i -= 1
        bigger_than_decreasing_index = i

        # swap bigger_than_decreasing_index and decreasing_index
        arr[bigger_than_decreasing_index], arr[decreasing_index] = \
            arr[decreasing_index], arr[bigger_than_decreasing_index]

        reverse(arr, decreasing_index+1, n-1)
        return


def main():
    arr = list(map(int, input().split()))

    # The function works in place
    find_next_permutation(arr)
    print(arr)


if __name__ == '__main__':
    main()
