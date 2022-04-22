# python 3

def can_split(arr, max_sum, max_split):
    count = 1
    curr_sum = 0

    for ele in arr:
        curr_sum += ele
        if curr_sum > max_sum:
            count += 1
            curr_sum = ele

        if count > max_split:
            return False

    return True


def find_min_subarray_sum(arr, m):
    low, high = max(arr), sum(arr)
    ans = -1

    while low <= high:
        mid = (low + high) // 2

        if can_split(arr, mid, m):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


def main():
    arr = list(map(int, input().split()))
    m = input()
    print(find_min_subarray_sum(arr, m))


if __name__ == '__main__':
    main()