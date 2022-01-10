# python 3

# Given N jobs where every job is represented by following three elements of it.
# 1. Start Time
# 2. Finish Time
# 3. Profit or Value Associated (>= 0)
# Find the maximum profit subset of jobs such that no two jobs in the subset overlap.

# Example:
# Input: Number of Jobs n = 4
#       Job Details {Start Time, Finish Time, Profit}
#       Job 1:  {1, 2, 50}
#       Job 2:  {3, 5, 20}
#       Job 3:  {6, 19, 100}
#       Job 4:  {2, 100, 200}
# Output: The maximum profit is 250.

# We can get the maximum profit by scheduling jobs 1 and 4.
# Note that there is longer schedules possible Jobs 1, 2 and 3
# but the profit with this schedule is 20+50+100 which is less than 250.


# Try to convert this to dp

def find_max_profit_recur(jobs, n):
    if n == 0:
        return jobs[0][2]

    curr_start_time = jobs[n][0]
    j = n - 1
    while j >= 0:
        if jobs[j][1] <= curr_start_time:
            break
        j -= 1

    profit_including_curr_job = jobs[n][2] + find_max_profit_recur(jobs, j)
    profit_excluding_curr_job = find_max_profit_recur(jobs, n-1)

    return max(profit_including_curr_job, profit_excluding_curr_job)


def find_max_profit(jobs):
    jobs.sort(key=lambda x: x[1])
    n = len(jobs)
    return find_max_profit_recur(jobs, n-1)


def main():
    num_jobs = int(input())
    jobs = []
    for i in range(num_jobs):
        jobs.append(list(map(int, input().split())))

    print(find_max_profit(jobs))


if __name__ == '__main__':
    main()
