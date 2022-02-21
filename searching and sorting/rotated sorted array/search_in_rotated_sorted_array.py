from typing import List
from find_min_in_rotated_sorted_array import find_min


def binary_search(nums: List[int], key: int, l: int, r: int) -> int:
    if not nums:
        return -1
    while l <= r:
        mid = (l + r) // 2
        if key == nums[mid]:
            return mid
        if key < nums[mid]:
            r = mid - 1
        else:
            l = mid + 1
    return -1


def search(nums: List[int], target: int) -> int:
    l = find_min(nums)
    if l == 0:
        l = len(nums) - 1
    else:
        l -= 1

    pos1 = binary_search(nums, target, 0, l)
    pos2 = binary_search(nums, target, l + 1, len(nums) - 1)

    return max(pos1, pos2)


def search_direct(nums, key):
    if not nums:
        return -1
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == key:
            return mid
        if nums[l] <= nums[mid]:
            if nums[l] <= key <= nums[mid]:
                r = mid - 1
            else:
                l = mid + 1
        else:
            if nums[mid] <= key <= nums[r]:
                l = mid + 1
            else:
                r = mid - 1
    return 'false'


def search_direct_duplicate(nums: List[int], key: int) -> bool:
    if not nums:
        return False
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] == key or nums[l] == key or nums[r] == key:
            return True
        if nums[l] < nums[mid]:
            if nums[l] <= key < nums[mid]:
                r = mid
            else:
                l = mid + 1
        elif nums[mid] > nums[l]:
            if nums[mid] < key < nums[r]:
                l = mid + 1
            else:
                r = mid
        else:
            l += 1
            r -= 1
    return False


l = [4, 5, 6, 7, 0, 1, 2]
key = 2
print(search(l, key))
