# python 3

# The approach should be optimized by using prefix array or storing the sum of entire array and using it multiple times
# rather than going from range l to r

def find_sum(arr, left, right):
    arr_sum = 0
    for i in range(left, right + 1):
        arr_sum += arr[(i-1) % len(arr)]

    return arr_sum


def find_sum_in_ranges(arr, n, queries):
    ans = []
    for left, right in queries:
        ans.append(find_sum(arr, left, right))

    return ans


def main():
    arr = list(map(int, input().split()))
    num_queries = int(input())

    queries = []
    for i in range(num_queries):
        queries.append(list(map(int, input().split())))

    print(find_sum_in_ranges(arr, len(arr), queries))


if __name__ == '__main__':
    main()
