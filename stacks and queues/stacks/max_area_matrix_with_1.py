# Python 3

def get_max_area(histogram):
    stack = []
    left = [0] * len(histogram)
    for i in range(len(histogram)):
        if not stack:
            left[i] = 0
            stack.append(i)
            continue
        top = stack[-1]
        while stack and histogram[top] >= histogram[i]:
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
        while stack and histogram[top] >= histogram[i]:
            stack.pop()
            if stack:
                top = stack[-1]
        if not stack:
            right[i] = len(histogram) - 1
        else:
            right[i] = top - 1
        stack.append(i)

    area = [0] * len(histogram)
    max_area = histogram[0]
    for i in range(1, len(histogram)):
        area[i] = (right[i] - left[i] + 1) * histogram[i]
        if area[i] > max_area:
            max_area = area[i]
    return max_area


def max_area(M, n, m):
    # code here
    maximum_area = 1

    for row in range(1, n):
        for column in range(m):

            if M[row][column] == 1:
                M[row][column] += M[row - 1][column]

        area = get_max_area(M[row])
        if area > maximum_area:
            maximum_area = area

    return maximum_area


def main():
    n, m = map(int, input().split())
    matrix = []
    for i in range(n):
        row = list(map(int, input().split()))
        matrix.append(row)
    print(max_area(matrix, n, m))


if __name__ == '__main__':
    main()