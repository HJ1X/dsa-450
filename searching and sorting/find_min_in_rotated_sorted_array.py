from typing import List


# all wrong
def find_min_with_duplicates(nums):
    l, r = 0, len(nums) - 1
    if nums[l] < nums[r]:
        return nums[0]

    while l <= r:

        mid = (l + r) // 2
        if l == r:
            return l
        if mid == 0:
            if nums[mid] > nums[mid + 1]:
                return mid + 1
            else:
                return mid

        if nums[mid - 1] > nums[mid]:
            return mid

        if nums[mid] < nums[r]:
            r = mid - 1
        elif nums[mid] > nums[l]:
            l = mid + 1
        else:
            l += 1


def find_min(nums: List[int]) -> int:
    l, r = 0, len(nums) - 1
    if nums[l] < nums[r]:
        return 0
    while l <= r:

        mid = (l + r) // 2
        if l == r:
            return l
        if mid == 0:
            if nums[mid] > nums[mid + 1]:
                return mid + 1
            else:
                return mid

        if nums[mid - 1] > nums[mid]:
            return mid

        if nums[mid] < nums[r]:
            r = mid - 1
        else:
            l = mid + 1


if __name__ == '__main__':
    # this function returns minimum index
    arr = list(map(int, input().split()))
    print(find_min(arr))


