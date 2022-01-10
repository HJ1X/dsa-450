# python 3

def max_product(arr, n):
    # code here

    max_prod = arr[0]  # 6
    min_till_now = arr[0]  # 6
    max_till_now = arr[0]  # 6

    for i in range(1, n):
        max_curr = max_till_now * arr[i]
        min_curr = min_till_now * arr[i]

        max_till_now = max(arr[i], min_curr, max_curr)
        min_till_now = min(arr[i], max_curr, min_curr)

        max_prod = max(max_till_now, max_prod)

    return max_prod


def main():
    arr = list(map(int, input().split()))
    print(max_product(arr, len(arr)))


if __name__ == '__main__':
    main()
