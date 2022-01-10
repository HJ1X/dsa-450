# python 3

from graph_basics import Graph


def create_undirected(graph):
    un_adj = [[] for i in range(len(graph.adj))]

    for u in range(len(graph.adj)):
        for v in graph.adj[u]:
            un_adj[u].append(v)
            un_adj[v].append(u)

    return un_adj


def find_wcc(graph):
    # Convert directed graph to undirected
    un_adj = create_undirected(graph)

    # Finding connected components for the undirected graph
    return graph.find_connected_components(un_adj)


def main():
    graph = Graph()
    print(find_wcc(graph))


if __name__ == '__main__':
    main()
