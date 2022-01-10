# python 3

# smallest subarray with sum greater than or equal to target |
# https://leetcode.com/problems/minimum-size-subarray-sum/submissions/

# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous
# subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no
# such subarray, return 0 instead.

def subarray_len(arr, target):
    if len(arr) == 1:
        if arr[0] >= target:
            return 1
        else:
            return 0

    min_size = float('inf')
    i, j = 0, 0
    window_sum = arr[0]

    while j < len(arr):
        if window_sum >= target:
            if i == j:
                return 1
            if min_size > j - i + 1:
                min_size = j - i + 1
            window_sum -= arr[i]
            i += 1

        else:
            j += 1
            if j < len(arr):
                window_sum += arr[j]

    if min_size == float('inf'):
        return 0
    return min_size


def main():
    arr = [12,28,83,4,25,26,25,2,25,25,25,12]
    target = 213
    print(subarray_len(arr, target))


if __name__ == '__main__':
    main()
