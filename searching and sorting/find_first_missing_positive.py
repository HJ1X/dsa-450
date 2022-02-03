# Python 3

# Find the first missing positive element in array from 1 to n | Leetcode - 41
from typing import List


def first_missing_positive(nums: List[int]) -> int:
    n = len(nums)
    for i in range(n):
        index = nums[i] - 1    # subtracting 1 due to zero based indexing

        # swapping element at i with its correct position i.e. nums[nums[i]-1]
        while 1 <= nums[i] <= n and nums[index] != nums[i]:
            nums[index], nums[i] = nums[i], nums[index]
            index = nums[i] - 1

    for i in range(n):
        if nums[i] != i + 1:
            return i + 1

    return n + 1


if __name__ == '__main__':
    arr = list(map(int, input().split()))
    print(first_missing_positive(arr))
