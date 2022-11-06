# python 3

def find_mid_sum(arr1, arr2, n):
    if n == 1:
        return arr1[0] + arr2[0]

    if len(arr2) < len(arr1):
        return find_mid_sum(arr2, arr1, n)

    low = 0
    high = n

    while low <= high:
        cut1 = (low + high) // 2
        cut2 = n - cut1

        left1 = arr1[cut1 - 1] if cut1 != 0 else float('-inf')
        left2 = arr2[cut2 - 1] if cut2 != 0 else float('-inf')

        right1 = arr1[cut1] if cut1 != n else float('inf')
        right2 = arr2[cut2] if cut2 != n else float('inf')

        if left1 <= right2 and left2 <= right1:
            return max(left1, left2) + min(right1, right2)

        elif left1 > right2:
            high = cut1 - 1
        else:
            low = cut1 + 1


def main():
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    find_mid_sum(arr1, arr2, len(arr1))


if __name__ == '__main__':
    main()
