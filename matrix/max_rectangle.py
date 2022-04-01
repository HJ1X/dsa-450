# python 3

def find_max_rectangle(arr):
    stack = []
    max_area = 0
    n = len(arr)

    for i in range(n+1):
        while stack and (i == n or arr[i] <= arr[stack[-1]]):
            height = arr[stack.pop()]
            left_limit = stack[-1] if stack else -1

            area = (i - left_limit - 1) * height
            max_area = max(area, max_area)

        stack.append(i)

    return max_area


def find_max_area(matrix, n, m):
    max_rectangle = find_max_rectangle(matrix[0])

    for row in range(1, n):
        for col in range(m):
            if matrix[row][col] == 1:
                matrix[row][col] += matrix[row - 1][col]

        max_rectangle = max(max_rectangle, find_max_rectangle(matrix[row]))

    return max_rectangle


def main():
    pass


if __name__ == '__main__':
    main()
