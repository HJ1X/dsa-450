# python 3

def generate_powerset_recursion_util(string, i, answer, powerset):
    if i == len(string):
        powerset.append(answer)
        return

    generate_powerset_recursion_util(string, i + 1, answer + string[i], powerset)    # choosing the character
    generate_powerset_recursion_util(string, i + 1, answer, powerset)              # not choosing character


def generate_powerset_recursion(string):
    powerset = []
    generate_powerset_recursion_util(string, 0, '', powerset)
    return powerset


def generate_powerset_bit_manipulation(arr):
    powerset_size = 2 ** len(arr)
    ans = []
    for i in range(powerset_size):
        j = i
        curr_ans = []
        count = 0
        while j > 0:
            if j & 1 == 1:
                curr_ans.append(ans[count])
            count += 1
            j >>= 1
        ans.append(curr_ans)

    return ans


def main():
    string = input()
    print(generate_powerset_recursion(string))


if __name__ == '__main__':
    main()
