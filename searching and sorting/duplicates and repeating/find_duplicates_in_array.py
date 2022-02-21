# python 3

# Find duplicates in the array. Print the duplicate numbers with their occurrences. | Leetcode - 442

# Approaches:
# 1. Brute-force:- For every element in array, traverse the array and check if duplicates are present
#           TC - O(N_sq)                            SC - O(1)
# 2. Sort the array and then check for duplicates in adjacent elements.
#           TC - O(NlogN)                           SC - O(1)
# 3. Using Hashmap or creating a count array. If frequency of an element is more than 1 print it.
#           TC - O(N)                               SC - O(N)
# 4. To reduce extra space from above approach use same array to store frequency.
#    Visit elements by using value of array and add n to it. To access original-value use arr[index] % n.
#    To get frequency divide value by n - arr[index] / n
#           TC - O(N)                               SC - O(1)

# In this code, frequency list is being returned, which could be changed to just print elements having count > 1

def find_duplicates(arr):
    n = len(arr) + 1
    ans = []

    for i in range(n - 1):
        index = (arr[i] - 1) % n
        arr[index] += n

    print(arr)
    for i in range(n - 1):
        element = i + 1
        count = arr[i] // n
        ans.append((element, count))

    return ans


def main():
    arr = list(map(int, input().split()))
    print(*find_duplicates(arr))


if __name__ == '__main__':
    main()
