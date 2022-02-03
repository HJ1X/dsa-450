# python 3

def merge_interval(arr):
    n = len(arr)
    res = []
    i = 0
    while i < n:
        j = i+1
        interval = [arr[i][0], arr[i][1]]
        while j < n and arr[j][0] <= interval[1]:
            interval[1] = arr[j][1]
            j += 1
        res.append(interval)
        i = j
    return res


def merge_overlapping_intervals(intervals):
    intervals.sort()
    i = 0
    n = len(intervals)
    new_intervals = []

    while i < n:
        curr_interval = [intervals[i][0]]     # interval to add in result
        right_limit = intervals[i][1]         # right limit of interval

        # Merging intervals till they are overlapping
        while i + 1 < n and right_limit >= intervals[i + 1][0]:
            # if right limit of next interval is greater, update right limit
            if right_limit < intervals[i + 1][1]:
                right_limit = intervals[i + 1][1]
            i += 1

        curr_interval.append(right_limit)     # Append right limit to interval
        new_intervals.append(curr_interval)   # Append interval to result
        i += 1

    return new_intervals


def main():
    arr = [[1, 4],[4, 5]]
    print(merge_interval(arr))


if __name__ == '__main__':
    main()