# python 3

# Queue based approach is not that efficient and even intuitive, so not implemented. Can try

def tour(dist, fuel, n):
    total_remaining, curr_remaining = 0, 0
    starting_point = 0

    for i in range(n):
        curr_remaining += fuel[i] - dist[i]
        total_remaining += curr_remaining

        if curr_remaining < 0:
            curr_remaining = 0
            starting_point = i + 1

    if total_remaining < 0:
        return -1
    else:
        return starting_point


def main():
    pass


if __name__ == '__main__':
    main()
