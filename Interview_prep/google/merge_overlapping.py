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

def main():
    arr = [[1,4],[4,5]]
    print(merge_interval(arr))


if __name__ == '__main__':
    main()