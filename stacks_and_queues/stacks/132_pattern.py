# python 3

def find_132_pattern(arr):
    stack = []   # pair (num, minValue), monotonically decreasing
    min_val = float('inf')

    for num in arr:
        while stack and stack[-1][0] <= num:
            stack.pop()

        if stack and num > stack[-1][1]:  # min_value before element at top of stack
            return True

        stack.append((num, min_val))
        min_val = min(min_val, num)

    return False


def main():
    arr = list(map(int, input().split()))
    print(find_132_pattern(arr))


if __name__ == '__main__':
    main()
