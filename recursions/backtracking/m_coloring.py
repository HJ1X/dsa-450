# python 3

def is_valid(graph, num_color, vertex, vertices, color):
    for i in range(vertices):
        if graph[vertex][i] == 1:
            if color[i] == num_color:
                return False

    return True


def can_color(graph, vertex, m, n, color):
    if vertex == n:
        return True

    for num_color in range(m):
        if is_valid(graph, num_color, vertex, n, color):
            color[vertex] = num_color
            if can_color(graph, vertex + 1, m, n, color):
                return True
            color[vertex] = None

    return False


def graph_coloring(graph, m, vertices):
    # Graph is expected as a adjacency matrix
    color = [None for i in range(vertices)]
    if can_color(graph, 0, m, vertices, color):
        return True
    else:
        return False


def main():
    pass


if __name__ == '__main__':
    main()
