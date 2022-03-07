# Python 3

# Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number
# of contiguous bars. For simplicity, assume that all bars have the same width and the width is 1 unit, there will be
# N bars height of each bar will be given by the array arr.

def get_max_area(arr):
    n = len(arr)

    stack = []
    left_height = [-1] * n
    for i in range(n):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()

        if stack:
            left_height[i] = stack[-1]

        stack.append(i)

    stack = []
    right_height = [n] * n
    for i in range(n - 1, -1, -1):
        while stack and arr[i] <= arr[stack[-1]]:
            stack.pop()

        if stack:
            right_height[i] = stack[-1]

        stack.append(i)

    max_area = 0
    for i in range(n):
        width = right_height[i] - left_height[i] - 1
        area = arr[i] * width
        max_area = max(area, max_area)

    return max_area


def get_max_area_efficient(arr):
    n = len(arr)
    stack = []
    max_area = 0

    for i in range(n):
        while stack and arr[i] <= arr[stack[-1]]:
            height = arr[stack.pop()]
            left_limit = stack[-1] if stack else -1

            area = (i - left_limit - 1) * height
            max_area = max(area, max_area)

        stack.append(i)

    while stack:
        height = arr[stack.pop()]
        left_limit = stack[-1] if stack else -1

        area = (n - left_limit - 1) * height
        max_area = max(area, max_area)

    return max_area


def main():
    arr = list(map(int, input().split()))
    print(get_max_area_efficient(arr))


if __name__ == '__main__':
    main()
