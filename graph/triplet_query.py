# python 3


def create_adj_list(edges, vertices):
    adj = [[] for i in range(vertices)]

    for edge in edges:
        adj[edge[0]].append(edge[1])
        adj[edge[1]].append(edge[0])

    return adj


def explore(vertex, adj, query, colors, visited, cities_visited):
    visited[vertex] = True
    for node in adj[vertex]:
        if not visited[node] and colors[node] in query:
            cities_visited.add(colors[node])
            explore(node, adj, query, colors, visited, cities_visited)


def has_path(adj, query, colors):
    vertex = -1
    for i in range(len(colors)):
        if colors[i] == query[0]:
            cities_visited = set()
            visited = [False] * len(adj)

            vertex = i
            cities_visited.add(colors[i])

            explore(vertex, adj, query, colors, visited, cities_visited)
            if len(cities_visited) == 3:
                return True

    return False


def solve(vertices, colors, edges, queries):
    # Create adj list
    adj = create_adj_list(edges, vertices)

    ans = []

    # Exploring
    for query in queries:
        if has_path(adj, query, colors):
            ans.append('YES')
        else:
            ans.append('NO')

    return ans


def main():
    edges = []
    vertices = 44
    queries = []

    colors = input()
    for i in range(178):
        edge = list(map(int, input().split()))
        edges.append(edge)

    for i in range(143):
        queries.append(input())

    print(solve(vertices, colors, edges, queries))


if __name__ == '__main__':
    main()
