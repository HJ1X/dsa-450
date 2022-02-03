# python 3

# kadane's algorithm

def largest_sum(arr):
    curr_sum = 0
    max_sum = arr[0]

    for i in range(len(arr)):
        curr_sum += arr[i]

        if curr_sum > max_sum:
            max_sum = curr_sum

        if curr_sum < 0:
            curr_sum = 0

    return max_sum


def main():
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(largest_sum(arr))


if __name__ == '__main__':
    main()
