# python 3

# You are given N number of books. Every ith book has Ai number of pages. You have to allocate contagious books to M
# number of students. There can be many ways or permutations to do so. In each permutation, one of the M students
# will be allocated the maximum number of pages. Out of all these permutations, the task is to find that particular
# permutation in which the maximum number of pages allocated to a student is minimum of those in all the other
# permutations and print this minimum value.
#
# Each book will be allocated to exactly one student. Each student has to be allocated at least one book. Note:
# Return -1 if a valid assignment is not possible, and allotment should be in contiguous order (see the explanation
# for better understanding).

# https://practice.geeksforgeeks.org/problems/allocate-minimum-number-of-pages0937/1 | O(nlogn)

def can_place_students(arr, students, max_pages):
    # count of students allocated books with maximum pages equals to max_pages
    count = 0

    pages_of_curr_student = arr[0]
    count += 1

    for i in range(1, len(arr)):

        # if arr[i] > max_pages:
        #      return False                  # In this condition loop should start from 0 not 1

        if arr[i] + pages_of_curr_student <= max_pages:
            pages_of_curr_student += arr[i]

        else:
            count += 1
            pages_of_curr_student = arr[i]

        if count > students:
            return False

    return True


def find_pages(arr, n, m):
    ans = 0
    arr.sort()

    low, high = max(arr), sum(arr)       # also low can be made 0 with an extra condition in above function
    while low <= high:
        mid = (low + high) // 2
        if can_place_students(arr, m, mid):
            ans = mid
            high = mid - 1

        else:
            low = mid + 1

    return ans


def can_allocate_pages(arr, children, max_pages):
    curr_allocation = 0
    children -= 1     # Allocating to first child

    for pages in arr:
        if curr_allocation + pages <= max_pages:
            curr_allocation += pages

        else:
            curr_allocation = pages
            children -= 1

        if children < 0:
            return False

    return True


def find_min_pages(arr, children):
    arr.sort()
    min_of_pages_allocated = float('inf')

    low = arr[-1]
    high = sum(arr)
    while low <= high:
        mid = (low + high) // 2
        if can_allocate_pages(arr, children, mid):
            min_of_pages_allocated = mid
            high = mid - 1
        else:
            low = mid + 1

    return min_of_pages_allocated


def main():
    n = 4
    arr = [12, 34, 67, 90]
    m = 2
    print(find_pages(arr, n, m))
    print(find_min_pages(arr, m))


if __name__ == '__main__':
    main()
