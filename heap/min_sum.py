# python 3

# Given an array Arr of size N such that each element is from the range 0 to 9. Find the minimum possible sum of two
# numbers formed using the elements of the array. All digits in the given array must be used to form the two numbers.

from heapq import heappush, heappop


def find_min_sum(arr):
    if len(arr) == 1:
        return arr[0]

    heap = []
    for ele in arr:
        heappush(heap, ele)

    num1, num2 = '', ''
    is_odd_turn = True

    while heap:
        ele = heappop(heap)

        if is_odd_turn:
            num1 += str(ele)
        else:
            num2 += str(ele)

        is_odd_turn = not is_odd_turn

    return int(num1) + int(num2)


def main():
    pass


if __name__ == '__main__':
    main()
