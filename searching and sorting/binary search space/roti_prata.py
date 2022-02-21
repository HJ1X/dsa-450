# python 3

# The first line tells the number of test cases. Each test case consist of 2 lines. In the first line of the test
# case we have P the number of prata ordered. In the next line the first integer denotes the number of cooks L and L
# integers follow in the same line each denoting the rank of a cook.

# https://www.spoj.com/problems/PRATA/  |  Uses binary search


def time_feasible(num_prata, num_cooks, cook_ranks, time_given):

    count_prata = 0
    for rank in cook_ranks:
        time_next_prata = rank
        time_frame = time_given
        i = 1
        while time_next_prata <= time_frame:
            count_prata += 1               # increasing count of prata
            time_frame -= i * rank         # decreasing time_frame by time taken to make current prata

            i += 1                         # increment count of prata
            time_next_prata = i * rank     # time for next prata

        if count_prata >= num_prata:
            return True

    return False


def find_time(num_prata, num_cooks, cook_ranks):
    ans = -1
    # Search space would be between 0 and time when cook with highest rank making all pratas
    low, high = 0, cook_ranks[-1] * (num_prata * (num_prata+1) // 2)

    while low <= high:
        mid = (low + high) // 2

        if time_feasible(num_prata, num_cooks, cook_ranks, mid):
            ans = mid
            high = mid - 1

        else:
            low = mid + 1

    return ans


def main():
    num_prata = int(input())
    cook_ranks = list(map(int, input().split()))
    cook_ranks.sort()
    print(find_time(num_prata, len(cook_ranks), cook_ranks))


if __name__ == '__main__':
    main()
