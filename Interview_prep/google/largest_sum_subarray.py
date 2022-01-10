# python 4

# kadane's algorithm

def largest_sum(arr):
    sum = 0
    max_sum = arr[0]

    for i in range(len(arr)):
        sum += arr[i]
        if sum < 0:
            sum = 0

        if sum > max_sum:
            max_sum = sum

    return max_sum


def main():
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    print(largest_sum(arr))


if __name__ == '__main__':
    main()
