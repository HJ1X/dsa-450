# python 3

def left_child(i):
    return 2 * i + 1


def right_child(i):
    return 2 * i + 2


def parent(i):
    return (i - 1) // 2


def sift_down(arr, i):
    n = len(arr)
    while i < n:
        max_index = i
        l = left_child(i)
        if l < n and arr[l] > arr[max_index]:
            max_index = l

        r = right_child(i)
        if r < n and arr[r] > arr[max_index]:
            max_index = r

        if i != max_index:
            arr[max_index], arr[i] = arr[i], arr[max_index]
            i = max_index
        else:
            break


def sift_up(arr, i):
    n = len(arr)
    while i > 0 and arr[i] > arr[parent(i)]:
        arr[i], arr[parent(i)] = arr[parent(i)], arr[i]
        i = parent(i)


def extract_max(arr):
    max_ele = arr[0]
    arr[0] = arr.pop()
    sift_down(arr, 0)

    return max_ele


def push(arr, ele):
    arr.append(ele)
    sift_up(arr, len(arr) - 1)


def pop(arr):
    return extract_max(arr)


def build_heap(arr, n):
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, i)


def kth_smallest(arr, n, k):
    # Your code goes here

    heap = []
    for r in range(n):
        for c in range(n):
            if len(heap) < k:
                push(heap, arr[r][c])

            else:
                if arr[r][c] < heap[0]:
                    pop(heap)
                    push(heap, arr[r][c])

    return pop(heap)


def main():
    arr = [[1]]
    # arr = [[16, 28, 60, 64],
    #        [22, 41, 63, 91],
    #        [36, 78, 87, 94],
    #        [27, 50, 87, 93]]
    k = 1
    print(kth_smallest(arr, len(arr), k))


if __name__ == '__main__':
    main()
