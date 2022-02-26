from typing import List
from find_min_in_rotated_sorted_array import find_min


def binary_search(nums, target, param, l):
    # returns key index using binary search else -1
    return -1


def search_inefficient(nums: List[int], target: int) -> int:
    l = find_min(nums)
    if l == 0:
        l = len(nums) - 1
    else:
        l -= 1

    pos1 = binary_search(nums, target, 0, l)
    pos2 = binary_search(nums, target, l + 1, len(nums) - 1)

    return max(pos1, pos2)


def binary_search_rotated(nums, key):
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


def binary_search_rotated_duplicate(nums: List[int], key: int) -> bool:
    if not nums:
        return False
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2

        if nums[mid] == key:
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

    return False


def search(arr: list, low: int, high: int, key: int):
    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        # Left portion is sorted
        if arr[low] < arr[mid]:
            if arr[low] <= key < arr[mid]:  # key can not be equal to arr[mid]
                high = mid - 1
            else:
                low = mid + 1

        # Right portion is sorted
        else:
            if arr[mid] < key <= arr[high]:  # key can not be equal to arr[mid]
                low = mid + 1
            else:
                high = mid - 1

    return -1


def search_duplicates(arr: List[int], key: int) -> bool:
    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return True

        if arr[low] == arr[mid] and arr[mid] == arr[high]:
            low += 1

        elif arr[low] <= arr[mid]:
            if arr[low] <= key < arr[mid]:
                high = mid - 1
            else:
                low = mid + 1

        else:
            if arr[mid] < key <= arr[high]:
                low = mid + 1
            else:
                high = mid - 1

    return False


def main():
    arr = [3, 1]
    key = 1
    print(search_duplicates(arr, key))
    # print(binary_search_rotated_duplicate(arr, key))


if __name__ == '__main__':
    main()
