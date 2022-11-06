# python 3

def three_sum(nums):
    nums.sort()
    ans = []

    i = 0
    while i < len(nums) - 1:
        j = i + 1
        k = len(nums) - 1

        while j < k:
            if nums[i] + nums[j] + nums[k] > 0:
                k -= 1

            elif nums[i] + nums[j] + nums[k] < 0:
                j += 1

            else:
                ans.append([nums[i], nums[j], nums[k]])
                curr_ele = nums[j]
                while j < k and nums[j] == curr_ele:
                    j += 1

        curr_ele = nums[i]
        while i < len(nums) - 1 and nums[i] == curr_ele:
            i += 1

    return ans


def main():
    arr = list(map(int, input().split()))
    print(three_sum(arr))


if __name__ == '__main__':
    main()
