# python 3

def max_product(arr, n):
    max_prod = arr[0]
    min_ending_here = 1
    max_ending_here = 1

    for ele in arr:
        max_curr = max_ending_here * ele
        min_curr = min_ending_here * ele

        max_ending_here = max(ele, min_curr, max_curr)
        min_ending_here = min(ele, max_curr, min_curr)

        max_prod = max(max_ending_here, max_prod)

    return max_prod


def main():
    arr = list(map(int, input().split()))
    print(max_product(arr, len(arr)))


if __name__ == '__main__':
    main()
