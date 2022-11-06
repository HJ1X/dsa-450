# python 3

def generate_subarrays(arr):
    n = len(arr)
    ans = []
    for i in range(n):
        subset = []
        for j in range(i, n):
            subset.append(arr[j])
            ans.append(subset.copy())

    return ans


def main():
    arr = list(map(int, input().split()))
    print(generate_subarrays(arr))


if __name__ == '__main__':
    main()
