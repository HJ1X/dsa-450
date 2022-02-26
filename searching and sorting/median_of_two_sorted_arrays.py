# python 3

def median_of_arrays(arr1, arr2):
    # code here

    n = len(arr1)
    m = len(arr2)

    if n > m:
        return median_of_arrays(arr2, arr1)

    low, high = 0, len(arr1)
    while low <= high:
        part1 = (low + high) // 2
        part2 = ((n + m + 1) // 2) - part1

        left1 = arr1[part1 - 1] if part1 != 0 else float('-inf')
        left2 = arr2[part2 - 1] if part2 != 0 else float('-inf')

        right1 = arr1[part1] if part1 != n else float('inf')
        right2 = arr2[part2] if part2 != m else float('inf')

        if left1 <= right2 and left2 <= right1:
            if (n + m) % 2 == 0:
                median = (max(left1, left2) + min(right1, right2)) / 2
                return median
            else:
                median = max(left1, left2)
                return median

        elif left1 > right2:
            high = part1 - 1
        else:
            low = part1 + 1


def kth_element(arr1, arr2, n, m, k):
    if n > m:
        return kth_element(arr2, arr1, m, n, k)

    low = max(0, k - m)  # If m < k then at least k-m elements needs to be picked up from arr1
    high = min(n, k)     # If k < n then, we cannot pick all elements from arr1 so, k is max limit

    while low <= high:
        part1 = (low + high) // 2
        part2 = k - part1

        # part1 and part2 shows where the partition line is. so, left pick part - 1 element
        left1 = arr1[part1 - 1] if part1 > 0 else float('-inf')
        left2 = arr2[part2 - 1] if part2 > 0 else float('-inf')

        # right picks element at position of part
        right1 = arr1[part1] if part1 < n else float('inf')
        right2 = arr2[part2] if part2 < m else float('inf')

        if left1 <= right2 and left2 <= right1:
            return max(left1, left2)

        elif left1 > right2:
            high = part1 - 1
        else:
            low = part1 + 1

    return -1


def main():
    arr1 = [2, 3, 4]
    arr2 = [4, 5, 6]
    print(median_of_arrays(arr1, arr2))


if __name__ == '__main__':
    main()
