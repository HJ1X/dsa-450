# python 3

def explore(vertex, adj, visited, topo_sort):
    visited.add(vertex)
    for node in adj[vertex]:
        if node not in visited:
            explore(node, adj, visited, topo_sort)

    topo_sort.append(vertex)


def find_order(dictionary, n):
    adj = {}

    # Creating graph
    for i in range(n - 1):
        word1 = dictionary[i]
        word2 = dictionary[i + 1]

        i = 0
        while word1[i] == word2[i]:
            i += 1

        u = word1[i]
        v = word2[i]

        if u in adj:
            adj[u].append(v)
        else:
            adj[u] = [v]

        if v not in adj:
            adj[v] = []

    # Finding topological sort
    visited = set()
    topo_sort = []
    for vertex in adj.keys():
        if vertex not in visited:
            explore(vertex, adj, visited, topo_sort)

    return reversed(topo_sort)


def main():
    dictionary = ["baa","abcd","abca","cab","cad"]
    print(find_order(dictionary, len(dictionary)))


if __name__ == '__main__':
    main()
