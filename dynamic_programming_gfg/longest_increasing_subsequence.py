# Python 3

from collections import deque

# The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given
# sequence such that all elements of the subsequence are sorted in increasing order. For example, the length of LIS
# for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.

# Approaches
# 1. Using recursion calculate max of all previous maximums till n-1 and add 1 if n > i.
#                  TC - exponential                   SC - O(1)
# 2. Using same approach in DP
#                  TC - O(N_sq)                       SC - O(N)
# 3. Best approach is https://www.geeksforgeeks.org/longest-monotonically-increasing-subsequence-size-n-log-n/
#                  Tc - O(NlogN)


class Data:
    def __init__(self, index, value, lis_len, subsequence):
        self.index = index
        self.value = value
        self.lis_len = lis_len
        self.subsequence = subsequence


def lis(arr, n):
    if n == 1:
        return 1

    max_lis = 1
    for i in range(n - 1):
        max_i = lis(arr, i + 1)
        if arr[i] < arr[n - 1]:
            max_i += 1
        if max_i > max_lis:
            max_lis = max_i

    return max_lis


def lis_dp(arr, n, dp):
    if n == 1:
        return 1
    max_lis = 1
    for i in range(n - 1):
        max_i = 1
        if dp[i] is None:
            max_i = lis_dp(arr, i+1, dp)
            dp[i] = max_i
        else:
            max_i = dp[i]
        if arr[i] < arr[n-1]:
            max_i += 1
        if max_i > max_lis:
            max_lis = max_i
    print(dp)
    return max_lis


def lis_dp_tabulation(arr, n, dp):
    dp[0] = 1
    for i in range(n):
        max_dp = 0
        for j in range(i):
            if dp[j] > max_dp and arr[j] < arr[i]:
                max_dp = dp[j]
        dp[i] = max_dp + 1

    max_lis = 0
    for curr_lis in dp:
        if curr_lis > max_lis:
            max_lis = curr_lis

    return max_lis


def lis_dp_print(arr, n, dp):
    dp[0] = 1
    overall_max = 0

    # Finding the maximum LIS by forming DP tabulation
    for i in range(n):
        max_dp = 0
        for j in range(i):
            if dp[j] > max_dp and arr[j] < arr[i]:
                max_dp = dp[j]

        # Simultaneously calculating overall maximum
        dp[i] = max_dp + 1
        if overall_max < dp[i]:
            overall_max = dp[i]

    # Adding maximum LIS values in queue (there can be more than one)
    subsequences = deque()
    for i in range(n):
        if dp[i] == overall_max:
            subsequences.append(Data(i, arr[i], dp[i], deque([arr[i]])))

    # Looping till queue becomes empty i.e all elements are visited
    while subsequences:
        # finding last element with maximum lis in queue
        last_element = subsequences.pop()

        # If lis of last element is 1 that means it should be last element of subsequence
        if last_element.lis_len == 1:
            print(last_element.subsequence)
            continue

        # looping to find all element for which lis == last_element.lis - 1 and also whose value is smaller than
        # last element's value
        for i in range(last_element.index - 1, -1, -1):
            if dp[i] == last_element.lis_len - 1 and arr[i] < last_element.value:
                sub_sq = last_element.subsequence.copy()
                sub_sq.appendleft(arr[i])

                # Adding the found element to the queue
                subsequences.appendleft(Data(i, arr[i], dp[i], sub_sq))

    return overall_max


def binary_search(key, arr):
    l = 1
    r = len(arr) - 1

    while l <= r:
        mid = (l + r) // 2
        if arr[mid] == key:
            return mid
        if key < arr[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return l


def lis_nlogn(arr, n):
    # lis_arr = [float('inf')] * (n+1)
    # lis_arr[0] = float('-inf')
    #
    # lis_arr[1] = arr[0]
    # for i in range(1, n):
    #     index = binary_search(arr[i], lis_arr)
    #     lis_arr[index] = arr[i]
    #
    # for i in range(n, 0, -1):
    #     if lis_arr[i] != float('inf'):
    #         return i

    lis = [arr[0]]
    for i in range(1, n):
        key = arr[i]
        low, high = 0, len(lis) - 1
        while low <= high:
            mid = (low + high) // 2

            if key <= lis[mid]:
                high = mid - 1
            else:
                low = mid + 1

        if low >= len(lis):
            lis.append(key)
        else:
            lis[low] = key

    return len(arr)


def main():
    arr = list(map(int, input().split()))
    # arr = [i for i in range(1000)]
    dp = [None] * len(arr)
    # print(lis_dp(arr, len(arr), dp))
    # print(lis_dp_print(arr, len(arr), dp))
    print(lis_nlogn(arr, len(arr)))


if __name__ == '__main__':
    main()
