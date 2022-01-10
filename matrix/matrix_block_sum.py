# python 3

# leetcode 1314

def cal_block_sum(mat, k):
    prefix_sum = []
    for i in range(len(mat)):
        sum_total = 0
        sum_temp = []
        for j in range(len(mat[0])):
            sum_total += mat[i][j]
            if i == 0:
                sum_temp.append(sum_total)
            else:
                sum_temp.append(sum_total + prefix_sum[i - 1][j])
        prefix_sum.append(sum_temp)

    answer = mat
    for i in range(len(mat)):
        for j in range(len(mat[0])):
            sum_ij = 0

            # calculate sum till (i+k, j+k):
            r = min(i + k, len(mat) - 1)
            c = min(j + k, len(mat[0]) - 1)
            sum_ij = prefix_sum[r][c]

            # subtract extra sum (i-k, j-k)
            r_lower = max(i - k, 0)
            c_lower = max(j - k, 0)

            if r_lower > 0:
                sum_ij -= prefix_sum[r_lower - 1][c]
            if c_lower > 0:
                sum_ij -= prefix_sum[r][c_lower - 1]

            # adding extra subtracted sum
            if r_lower > 0 and c_lower > 0:
                sum_ij += prefix_sum[r_lower - 1][c_lower - 1]

            answer[i][j] = sum_ij

    return answer


def main():
    mat = [[1,2,3],[4,5,6],[7,8,9]]
    k = 1
    print(cal_block_sum(mat, k))


if __name__ == '__main__':
    main()
