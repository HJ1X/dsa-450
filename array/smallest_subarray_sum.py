# python 3

# smallest subarray with sum greater than or equal to target |
# https://leetcode.com/problems/minimum-size-subarray-sum/submissions/

# Given an array of positive integers nums and a positive integer target, return the minimal length of a contiguous
# subarray [numsl, numsl+1, ..., numsr-1, numsr] of which the sum is greater than or equal to target. If there is no
# such subarray, return 0 instead.

def subarray_len(arr, target):
    min_size = len(arr) + 1
    i, j = 0, 0
    window_sum = 0

    while j < len(arr):
        if window_sum >= target:
            if min_size > j - i:
                min_size = j - i
            window_sum -= arr[i]
            i += 1

        else:
            window_sum += arr[j]
            j += 1

    if min_size == len(arr) + 1:
        return 0
    else:
        return min_size


def subarray_sum(arr, n, s):
    i, j = 0, 0
    curr_sum = 0

    while j < n or curr_sum >= s:
        if curr_sum == s:
            return i + 1, j

        elif curr_sum < s:
            curr_sum += arr[j]
            j += 1

        else:
            curr_sum -= arr[i]
            i += 1

    return [-1]


def find_subarray_sum(arr, n, target):
    hash_map = {}
    curr_sum = 0
    count = 0

    for i in range(n):
        curr_sum += arr[i]
        if curr_sum - target in hash_map:
            count += hash_map[curr_sum-target]
        if curr_sum == target:
            count += 1

        if curr_sum in hash_map:
            hash_map[curr_sum] += 1
        else:
            hash_map[curr_sum] = 1

    return count


def main():
    arr = list(map(int, input().split()))
    target = -3
    # print(subarray_len(arr, target))
    # print(subArraySum(arr, len(arr), target))
    print(find_subarray_sum(arr, len(arr), target))


if __name__ == '__main__':
    main()
