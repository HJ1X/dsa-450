# python 3

class Solution:
    # Function to return k largest elements from an array.

    # This approach is good if we want to print the k largest element else, if we only need to find the kth largest
    # element than, quick select approach is better - TC - O(N) average

    # This approach creates max-heap from entire array and they extract max k times so, TC = n + klogn
    # Better approach is to just create a min-heap of size k and use it. ( on gfg practice )  TC = O((n-k)log(k))

    def left_child(self, i):
        return (2 * i) + 1

    def right_child(self, i):
        return (2 * i) + 2

    def parent(self, i):
        return (i - 1) // 2

    def sift_down(self, arr, i):
        n = len(arr)
        while i < n:
            max_index = i
            l = self.left_child(i)
            if l < n and arr[l] > arr[max_index]:
                max_index = l

            r = self.right_child(i)
            if r < n and arr[r] > arr[max_index]:
                max_index = r

            if i != max_index:
                arr[max_index], arr[i] = arr[i], arr[max_index]
                i = max_index
            else:
                break

    def extract_max(self, arr):
        max_ele = arr[0]
        arr[0] = arr.pop()
        self.sift_down(arr, 0)

        return max_ele

    def build_heap(self, arr, n):
        for i in range(n // 2, -1, -1):
            self.sift_down(arr, i)

    def k_largest(self, arr, n, k):
        # code here
        res = []

        self.build_heap(arr, n)
        for i in range(k):
            res.append(self.extract_max(arr))

        return res


def main():
    n, k = map(int, input().split())
    arr = list(map(int, input().split()))
    sol = Solution()
    print(*sol.k_largest(arr, n, k))


if __name__ == '__main__':
    main()
