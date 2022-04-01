# python 3

def copy_bits(x, y, l, r):
    # Converting to 0-based index
    l -= 1
    r -= 1

    bits = (y >> l) & ((1 << (r-l+1)) - 1)
    mask = bits << l

    return x | mask


def main():
    x, y, l, r = map(int, input().split())
    print(copy_bits(x, y, l, r))


if __name__ == '__main__':
    main()
