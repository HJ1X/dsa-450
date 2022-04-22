# python 3

def rearrange_hash_set(arr):
    neg_elements = []
    pos_elements = []

    for ele in arr:
        if ele < 0:
            neg_elements.append(ele)
        else:
            pos_elements.append(ele)

    i, j, k = 0, 0, 0
    while i < len(pos_elements) and j < len(neg_elements):
        arr[k] = pos_elements[i]
        arr[k + 1] = neg_elements[j]
        i += 1
        j += 1
        k += 2

    while i < len(pos_elements):
        arr[k] = pos_elements[i]
        k += 1
        i += 1

    while j < len(neg_elements):
        arr[k] = neg_elements[j]
        k += 1
        j += 1


def rearrange_hash_set_2(res):
    neg_elements = []
    pos_elements = []

    for ele in res:
        if ele < 0:
            neg_elements.append(ele)
        else:
            pos_elements.append(ele)

    i, j, k = 0, 0, 0
    arr = []

    while i < len(pos_elements) and j < len(neg_elements):
        arr.append(pos_elements[i])
        arr.append(neg_elements[j])
        i += 1
        j += 1

    while i < len(pos_elements):
        arr.append(pos_elements[i])
        i += 1

    while j < len(neg_elements):
        arr.append(neg_elements[j])
        j += 1

    res[:] = arr


def rotate(arr, left, right):
    val = arr[right]
    while right > left:
        arr[right] = arr[right - 1]
        right -= 1
    arr[left] = val
    return


def rearrange(arr, n):
    i = 0
    while i < n - 1:
        if (
            (i % 2 == 0 and arr[i] < 0) or
            (i % 2 != 0 and arr[i] >= 0)
        ):
            out_of_place_index = i
            j = i + 1
            while (
                    (j < n and arr[out_of_place_index] >= 0 and arr[j] >= 0) or
                    (j < n and arr[out_of_place_index] < 0 and arr[j] < 0)
            ):
                j += 1

            if j >= n:
                return
            rotate(arr, out_of_place_index, j)

        i += 1


def rearrange_2(arr, n):
    out_of_place = -1
    for index in range(n):
        if out_of_place >= 0:
            if (
                    arr[index] >= 0 > arr[out_of_place] or
                    arr[index] < 0 <= arr[out_of_place]
            ):
                rotate(arr, out_of_place, index)
                if index - out_of_place > 2:
                    out_of_place += 2
                else:
                    out_of_place = - 1
        if out_of_place == -1:
            if ((arr[index] >= 0 and index % 2 != 0) or
                    (arr[index] < 0 and index % 2 == 0)):
                out_of_place = index
    return arr


def main():
    arr = list(map(int, input().split()))
    rearrange(arr, len(arr))
    print(arr)


if __name__ == '__main__':
    main()
