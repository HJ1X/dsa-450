# Python 3

# In the given unsorted array find a pair whose difference equal given n and sum equal given n.

# Approaches
# 1. For every i traverse every j from i+1 to n and check if it equal sum or difference
#                   TC - O(N_sq)                         SC - O(1)
# 2. Sort the array and then traverse array from left to right. For every i binary search for number
# where i + j = n or j - i = n
#                   TC - O(NlogN) + O(NlogN)             SC - O(1)
# 3. Use two pointer approach to find pair after sorting. Given below
#                   TC - O(NlogN) + O(N)                 SC - O(1)

def find_sum(n, arr):
    arr.sort()
    i, j = 0, len(arr) - 1

    while i < j:
        if arr[i] + arr[j] == n:
            return True

        if arr[i] + arr[j] > n:
            j -= 1
        else:
            i += 1
    return False


def find_diff(n, arr):
    arr.sort()
    i, j = 0, 1

    while j < len(arr):
        if arr[j] - arr[i] == n:
            return True

        if arr[j] - arr[i] < n:
            j += 1
        else:
            i += 1
    return False


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    print(find_sum(n, arr))


if __name__ == '__main__':
    main()
