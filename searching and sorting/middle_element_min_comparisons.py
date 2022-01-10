# Python 3

def middle(A, B, C):
    # code here

    max_element = max(A, B, C)
    min_element = min(A, B, C)

    return A + B + C - max_element - min_element

    # if A<B:
    #     if B<C:
    #         return B
    #     else:
    #         return max(A,C)
    # if A<C:
    #     return A
    # else:
    #     return max(B,C)


if __name__ == '__main__':
    a, b, c = list(map(int, input().split()))
    print(middle(a, b, c))