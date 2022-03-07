# python 3

from heapq import heappush, heappop


def reorganize_string(s: str) -> str:
    # Populating hash map
    hash_map = {}
    for char in s:
        hash_map[char] = hash_map.setdefault(char, 0) + 1

    # Populating heap
    heap = []
    for char, freq in hash_map.items():
        heappush(heap, (-freq, char))

    # Building solution
    res = []
    i = 0
    while len(heap) > 1:      # At least two elements in heap
        count_curr, char_curr = heappop(heap)
        count_next, char_next = heappop(heap)

        count_curr *= -1
        count_next *= -1

        res.append(char_curr)
        res.append(char_next)

        if count_curr > 1:
            heappush(heap, (-(count_curr - 1), char_curr))
        if count_next > 1:
            heappush(heap, (-(count_next - 1), char_next))

    # If there is still element left, then, if its count is more we have
    # to put it adjacent, since, only one character is left. If its count is 1 then, no issues.
    if heap:
        count, char = heappop(heap)
        count *= -1

        if count > 1:
            return ''
        res.append(char)

    return ''.join(res)


def main():
    print(reorganize_string(input()))


if __name__ == '__main__':
    main()
