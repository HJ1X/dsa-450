# python 3

def babylonian_method(n):
    x = n
    y = 1
    accuracy = 0.000001
    while x - y > accuracy:
        x = (x + y) / 2
        y = n / x
    return float('{:.4f}'.format(x))


# Write a function to find number of perfect squares less than N
def square_root(n):
    x = babylonian_method(n)
    if x == int(x):
        return int(x - 1)
    else:
        return int(x)


if __name__ == '__main__':
    n = int(input())
    print(babylonian_method(n))