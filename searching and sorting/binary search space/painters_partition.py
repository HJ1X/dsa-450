# python 3

def can_allocate_boards(arr, painters, max_time):
    n = len(arr)
    count = 1

    curr_time = 0

    for i in range(n):
        if arr[i] > max_time:
            return False

        if curr_time + arr[i] <= max_time:
            curr_time += arr[i]

        else:
            count += 1
            curr_time = arr[i]

        if count > painters:
            return False

    return True


def number_of_painters(arr, n, max_len):
    total = 0
    numPainters = 1

    for i in arr:
        total += i

        if total > max_len:
            # for next count
            total = i
            numPainters += 1

    return numPainters


def min_time(arr, n, k):
    # ans = -1
    # low, high = 0, int(10e9)
    # while low <= high:
    #     mid = (low + high) // 2
    #     if can_allocate_boards(arr, k, mid):
    #         ans = mid
    #         high = mid - 1
    #     else:
    #         low = mid + 1
    # return ans

    lo = max(arr)
    hi = sum(arr)
    while lo < hi:
        mid = lo + (hi - lo) // 2
        requiredPainters = number_of_painters(arr, n, mid)
        if requiredPainters <= k:
            hi = mid
        else:
            lo = mid + 1
    return lo


def main():
    arr = [5, 10, 30, 20, 15]
    k = 3
    print(min_time(arr, len(arr), k))


if __name__ == '__main__':
    main()
