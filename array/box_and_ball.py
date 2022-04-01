# python 3

# We have N boxes, numbered 1 through N. At first, box 1 contains one red ball, and each of the other boxes contains
# one white ball. Snuke will perform the following M operations, one by one. In the i-th operation, he randomly picks
# one ball from box x i, then he puts it into box y i .
#
# Find the number of boxes that may contain the red ball after all operations are performed

def switch_balls(moves, num_bags):
    num_balls = [1 for i in range(num_bags)]
    can_have_red = [True if i == 0 else False for i in range(num_bags)]

    for from_bag, to_bag in moves:
        num_balls[from_bag-1] -= 1
        num_balls[to_bag-1] += 1

        if can_have_red[from_bag-1]:
            can_have_red[to_bag-1] = True

            if num_balls[from_bag-1] == 0:
                can_have_red[from_bag-1] = False

    count = 0
    for has_red in can_have_red:
        if has_red:
            count += 1

    return count


def main():
    n, q = map(int, input().split())
    moves = []
    for i in range(q):
        move = list(map(int, input().split()))
        moves.append(move)

    print(switch_balls(moves, n))


if __name__ == '__main__':
    main()
