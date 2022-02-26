# python 3

# Given an array of length ‘N’, where each element denotes the position of a stall. Now you have ‘N’ stalls and an
# integer ‘K’ which denotes the number of cows that are aggressive. To prevent the cows from hurting each other,
# you need to assign the cows to the stalls, such that the minimum distance between any two of them is as large as
# possible. Return the largest minimum distance.

# https://www.codingninjas.com/codestudio/problems/aggressive-cows_1082559?leftPanelTab=0 | TC = O(nlogn)


def can_place_cows(stalls, num_cows, dist):
    last_cow = 0
    num_cows -= 1

    for curr_pos in range(len(stalls)):
        if stalls[curr_pos] - stalls[last_cow] >= dist:
            num_cows -= 1
            last_cow = curr_pos

        if num_cows == 0:
            return True

    return False


def aggressive_cows(stalls, k):
    stalls.sort()
    max_dist = 0

    low = 0
    high = stalls[-1]
    while low <= high:
        mid = (low + high) // 2

        if can_place_cows(stalls, k, mid):
            max_dist = mid
            low = mid + 1

        else:
            high = mid - 1

    return max_dist


# def can_place_cows(arr, cows, dist):
#     # placed 1st cow at 1st stall
#     pos_last_placed_cow = 0
#     count = 1
#
#     for i in range(1, len(arr)):
#         if arr[i] - arr[pos_last_placed_cow] >= dist:
#             pos_last_placed_cow = i
#             count += 1
#
#         if cows == count:
#             return True
#
#     return False
#
#
# def aggressive_cows(stalls, k):
#     # Write your code here.
#
#     stalls.sort()
#     ans = 0
#
#     low, high = 0, stalls[len(stalls) - 1] - stalls[0]
#     while low <= high:
#         mid = (low + high) >> 1
#
#         if can_place_cows(stalls, k, mid):
#             ans = mid
#             low = mid + 1
#
#         else:
#             high = mid - 1
#
#     return ans


def main():
    stalls = list(map(int, input().split()))
    cows = 4
    print(aggressive_cows(stalls, cows))


if __name__ == '__main__':
    main()

