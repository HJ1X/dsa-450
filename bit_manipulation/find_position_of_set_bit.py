# python 3

def find_position(n):
    set_bit_count = 0
    bit_pos = 1
    ans = -1

    while n > 0:
        if n & 1 > 0:
            if set_bit_count == 1:
                return -1
            set_bit_count += 1
            ans = bit_pos

        n >>= 1
        bit_pos += 1

    return ans


def main():
    print(find_position(int(input())))


if __name__ == '__main__':
    main()
