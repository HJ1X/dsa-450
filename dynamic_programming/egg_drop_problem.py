# python 3

def print_min_moves(eggs, floors):
    dp = [[0 for i in range(floors + 1)] for j in range(eggs + 1)]

    for egg in range(1, eggs + 1):
        for floor in range(1, floors + 1):

            if floor == 1:
                dp[egg][floor] = 1

            elif egg == 1:
                dp[egg][floor] = floor

            else:
                min_moves = float('inf')
                for k in range(1, floor + 1):  # floor from where egg is dropping
                    if_broken = dp[egg - 1][k - 1]
                    if_not_broken = dp[egg][floor - k]

                    max_moves_at_k = max(if_broken, if_not_broken) + 1
                    if max_moves_at_k < min_moves:
                        min_moves = max_moves_at_k

                dp[egg][floor] = min_moves

    return dp[eggs][floors]


def main():
    eggs, floors = map(int, input().split())
    print(print_min_moves(eggs, floors))


if __name__ == '__main__':
    main()
