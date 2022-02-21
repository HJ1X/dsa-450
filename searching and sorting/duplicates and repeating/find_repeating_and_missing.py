# python 3

# Best solution is using XOR operations | GFG

def find_rep_and_miss_xor(n, arr):
    xor = 0
    for i in range(n):
        xor ^= arr[i]
        xor ^= i + 1

    # now, xor contains miss_num ^ repeat_num
    # finding rightmost set bit
    mask = xor & -xor
    num1 = 0
    num2 = 0

    for i in range(n):
        if mask & arr[i] > 0:
            num1 ^= arr[i]
        else:
            num2 ^= arr[i]

        if mask & (i + 1) > 0:
            num1 ^= i + 1
        else:
            num2 ^= i + 1

    for i in range(n):
        if arr[i] == num1:
            return num1, num2
    return num2, num1


def find_rep_and_miss_using_two_equation(n, arr):
    # This way causes issues for large float numbers

    sum_n = 0
    prod_n = 1

    for i in range(n):
        sum_n += i + 1
        sum_n -= arr[i]
        prod_n *= i + 1
        prod_n /= arr[i]

    y = sum_n / (prod_n - 1)
    x = y + sum_n

    return round(y), round(x)


def find_rep_and_miss_using_two_equation_sum_and_sum_of_squares(n, arr):
    sum_n = 0
    sum_n_sq = 0

    # Calculating ES - S = y - x and ES_sq - S_sq = y_sq - x_sq
    for i in range(n):
        sum_n += i + 1
        sum_n -= arr[i]
        sum_n_sq += (i+1) ** 2
        sum_n_sq -= arr[i] * arr[i]

    # sum_n denotes ES - S and sum_n_sq denotes ES_sq - S_sq
    y = (sum_n + (sum_n_sq // sum_n)) // 2
    x = y - sum_n

    return x, y


def find_rep_and_miss_using_elements_as_index(n, arr):
    # In this approach use elements as index and mark visited numbers as negatives
    # As we are marking visited elements as negatives we need to take absolute values of elements as index

    repeat_element = -1
    for i in range(n):
        if arr[abs(arr[i]) - 1] < 0:
            repeat_element = abs(arr[i])
            continue
        arr[abs(arr[i]) - 1] *= -1

    missing_element = -1
    for i in range(n):
        if arr[i] > 0:
            missing_element = i + 1
            break

    return repeat_element, missing_element


def main():
    n = int(input())
    arr = list(map(int, input().split()))
    # print(*find_rep_and_miss_xor(n, arr))
    print(find_rep_and_miss_using_elements_as_index(n, arr))

if __name__ == '__main__':
    main()