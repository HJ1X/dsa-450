# python 3

def max_sum(arr, n):
    total_sum = sum(arr)
    curr_val = 0

    # Initial value of configuration
    for i in range(n):
        curr_val += arr[i] * i

    ans = curr_val
    for i in range(n):
        # It doesn't matter if you rotate first element to end
        # or last element to first (right-rotate or left-rotate),
        # as we are considering all the configurations
        next_val = curr_val + total_sum - (n * arr[n - i - 1])
        # next_val = curr_val - total_sum + (n * arr[i])

        ans = max(next_val, ans)
        curr_val = next_val

    return ans


def main():
    pass


if __name__ == '__main__':
    main()
