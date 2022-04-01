# python 3

def max_sum_with_k(arr, n, k):
    max_sum_arr = []
    curr_sum = 0

    for ele in arr:
        curr_sum += ele
        max_sum_arr.append(curr_sum)

        if curr_sum < 0:
            curr_sum = 0

    ans = 0
    window_sum = 0

    for i in range(n):
        if i < k:
            window_sum += arr[i]
            ans = window_sum
        else:
            window_sum += arr[i] - arr[i - k]
            # Use window_sum + max_sum_arr[i-k] as max sum of subarray with
            # at least k elements is required
            ans = max(ans, window_sum, window_sum + max_sum_arr[i-k])

    return ans


def main():
    arr = list(map(int, input().split()))
    k = int(input())
    print(max_sum_with_k(arr, len(arr), k))


if __name__ == '__main__':
    main()
