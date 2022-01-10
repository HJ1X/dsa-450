# python 3

# In this problem, given two sorted arrays of length n and m, merge them as two sorted arrays i.e.
# 1st array will be containing elements from 1 to n and second from n + 1 to n + m in sorted fashion

# Three approaches could be used:
# 1. Create array of size n + m. Insert all elements. Sort this array. At last, fill arr1 and arr2 from this array
#       TC - O(NlogN) + O(N) + O(N)         SC - O(N + M)
# 2. Using insertion sort approach. iterate arr1 with i. For every i, iterate j in arr2. If arr[i] > arr[j], then
#    swap elements and insert element at arr[j] in correct position in arr2. Increment i.
#       TC - O(n * m)                       SC - O(1)
# 3. Using shell sort approach.
#       TC - O(NlogN)                       SC - O(1)

def merge_gfg(ar1, ar2):
    m = len(ar1)
    n = len(ar2)
    # Iterate through all
    # elements of ar2[] starting from
    # the last element
    for i in range(n - 1, -1, -1):

        # Find the smallest element
        # greater than ar2[i]. Move all
        # elements one position ahead
        # till the smallest greater
        # element is not found
        last = ar1[m - 1]
        j = m - 2
        while j >= 0 and ar1[j] > ar2[i]:
            ar1[j + 1] = ar1[j]
            j -= 1

        # If there was a greater element
        if j != m - 2 or last > ar2[i]:
            ar1[j + 1] = ar2[i]
            ar2[i] = last
    return ar1, ar2


def merge_gfg_2(arr1, arr2):
    i, j, k = 0, 0, len(arr1)-1
    while i <= k and j < len(arr2):
        if arr1[i] < arr2[j]:
            i += 1
        else:
            arr2[j], arr1[k] = arr1[k], arr2[j]
            k -= 1
            j += 1
    arr1.sort()
    arr2.sort()
    return arr1, arr2


def merge(arr1, arr2):
    n, m = len(arr1), len(arr2)
    gap = (n + m) // 2

    while gap > 0:
        i = 0
        while i + gap < n + m:
            j = i + gap
            if i < n and j < n:
                x = i
                while x >= 0:
                    if arr1[j] >= arr1[x]:
                        break
                    arr1[j], arr1[x] = arr1[x], arr1[j]
                    x -= gap
                    j -= gap

            elif i < n and j >= n:
                j -= n
                x = i
                while x >= 0:
                    if arr2[j] >= arr1[x]:
                        break
                    arr2[j], arr1[x] = arr1[x], arr2[j]
                    x -= gap
                    j -= gap

            else:
                x = i - n
                j -= n
                while x >= 0:
                    if arr2[j] >= arr2[x]:
                        break
                    arr2[j], arr2[x] = arr2[x], arr2[j]
                    x -= gap
                    j -= gap

                if x < 0:
                    x += n
                    if arr2[j] >= arr1[x]:
                        continue
                    arr2[j], arr1[x] = arr1[x], arr2[j]
                    x -= gap
                    j = j - gap + n
                    print(x, j)
                    while x >= 0:
                        if arr1[j] >= arr1[x]:
                            break
                        arr1[j], arr1[x] = arr1[x], arr1[j]
                        x -= gap
            i += 1
        gap //= 2

    return arr1, arr2


def main():
    arr1 = list(map(int, input().split()))
    arr2 = list(map(int, input().split()))
    res1_arr, res2_arr = merge_gfg_2(arr1, arr2)
    print(*res1_arr)
    print(*res2_arr)


if __name__ == '__main__':
    main()