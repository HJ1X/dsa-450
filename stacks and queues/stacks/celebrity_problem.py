# python 3

def find_celebrity_stack(matrix, n):
    stack = []
    for i in range(n):
        stack.append(i)

    while len(stack) > 1:
        ele1 = stack.pop()
        ele2 = stack.pop()

        if matrix[ele1][ele2] == 1:
            stack.append(ele2)
        else:
            stack.append(ele1)

    candidate = stack.pop()
    for i in range(n):
        if i != candidate and matrix[i][candidate] == 0 or matrix[candidate][i] == 1:
            return -1

    return candidate


def knows(mat, i, j):
    if mat[i][j] == 1:
        return True
    else:
        return False


def find_celebrity_efficient(matrix, n):
    candidate = 0
    for i in range(1, n):
        if knows(matrix, candidate, i):
            candidate = i
    for i in range(n):
        if i != candidate and not knows(matrix, i, candidate):
            return -1
    return candidate


def main():
    pass


if __name__ == '__main__':
    main()
