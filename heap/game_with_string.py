# python 3
from heapq import heappush, heappop


def min_value(string, k):
    heap = []
    hash_map = {}

    # Adding values in hash_map
    for char in string:
        hash_map[char] = hash_map.get(char, 0) + 1

    # Creating priority queue for frequencies
    for key, value in hash_map.items():
        heappush(heap, (-value, key))

    # Decrementing count of top element k times
    for i in range(k):
        count, char = heappop(heap)
        heappush(heap, (count + 1, char))

    # calculating ans i.e. sum of squares of count of each character
    ans = 0
    while heap:
        ans += heappop(heap)[0] ** 2

    return ans


def main():
    pass


if __name__ == '__main__':
    main()
