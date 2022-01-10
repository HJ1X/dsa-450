# Python 3

# Find the largest rectangular area possible in a given histogram where the largest rectangle can be made of a number
# of contiguous bars. For simplicity, assume that all bars have the same width and the width is 1 unit, there will be
# N bars height of each bar will be given by the array arr.

def get_max_area(histogram):
    stack = []

    left = [0] * len(histogram)
    for i in range(len(histogram)):
        if not stack:
            left[i] = 0
            stack.append(i)
            continue

        top = stack[-1]
        while stack and histogram[top] > histogram[i]:
            stack.pop()
            if stack:
                top = stack[-1]

        if not stack:
            left[i] = 0
        else:
            left[i] = top + 1
        stack.append(i)

    stack = []

    right = [0] * len(histogram)
    for i in range(len(histogram) - 1, -1, -1):

        if not stack:
            right[i] = len(histogram) - 1
            stack.append(i)
            continue

        top = stack[-1]
        while stack and histogram[top] > histogram[i]:
            stack.pop()
            if stack:
                top = stack[-1]

        if not stack:
            right[i] = len(histogram) - 1
        else:
            right[i] = top - 1
        stack.append(i)

        # j = i
        # while j < len(histogram):
        #     if histogram[i] > histogram[j]:
        #         break
        #     j += 1
        # right[i] = j

    area = [0] * len(histogram)
    max_area = histogram[0]
    for i in range(1, len(histogram)):
        area[i] = (right[i] - left[i] + 1) * histogram[i]
        if area[i] > max_area:
            max_area = area[i]

    # print(left)
    # print(right)
    # print(area)
    return max_area


def main():
    arr = list(map(int, input().split()))
    print(get_max_area(arr))


if __name__ == '__main__':
    main()
