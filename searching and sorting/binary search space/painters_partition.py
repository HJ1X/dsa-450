# python 3

def can_allocate_boards(arr, painters, max_time):
    n = len(arr)
    count = 1
    curr_time = 0

    for i in range(n):
        if curr_time + arr[i] <= max_time:
            curr_time += arr[i]

        else:
            count += 1
            curr_time = arr[i]

        if count > painters:
            return False

    return True


def min_time(arr, n, k):
    ans = -1
    low, high = 0, int(10e9)

    while low <= high:
        mid = (low + high) // 2

        if can_allocate_boards(arr, k, mid):
            ans = mid
            high = mid - 1
        else:
            low = mid + 1

    return ans


def calculate_num_painters(arr, max_paint_area):
    count = 1
    curr_board_sum = 0

    for board_size in arr:
        if curr_board_sum + board_size > max_paint_area:
            count += 1
            curr_board_sum = board_size

        else:
            curr_board_sum += board_size

    return count


def min_time_required(arr, k):
    ans = None

    low = max(arr)
    high = sum(arr)

    while low <= high:
        mid = (low + high) // 2
        painters_required = calculate_num_painters(arr, mid)

        if painters_required <= k:
            high = mid - 1
            ans = mid
        else:
            low = mid + 1

    return ans


def main():
    arr = [5, 10, 30, 20, 15]
    k = 3
    print(min_time(arr, len(arr), k))


if __name__ == '__main__':
    main()
