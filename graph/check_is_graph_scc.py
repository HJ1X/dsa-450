# python 3

# Write a program to check if the given graph is a strongly connected component.
# https://www.geeksforgeeks.org/connectivity-in-a-directed-graph/

# Approach:
# 1. A simple idea is to use a all-pair-shortest path algorithm like Floyd Warshall or find Transitive
#    Closure of graph. Time complexity of this method would be O(v3).
# 2. We can also do DFS V times starting from every vertex. If any DFS, doesn’t visit all vertices, then graph is not
#    strongly connected. This algorithm takes O(V*(V+E)) time which can be same as transitive closure for a dense graph.
# 3. A better idea can be Strongly Connected Components (SCC) algorithm. We can find all SCCs in O(V+E) time.
#    If number of SCCs is one, then graph is strongly connected. The algorithm for SCC does extra work as it finds all
#    SCCs.
# 4. A better approach using two DFS:-
#       1. Perform DFS. If DFS does not visit all vertices return False.
#       2. Reverse Graph.
#       3. Perform DFS on reversed graph from same vertex as step 1. If DFS does not visit all vertices return False
#          else return True. O(V+E)

# Miscellaneous:
# 1. The above approach requires two traversals of graph. We can find whether a graph is strongly connected or not
#    in one traversal using Tarjan’s Algorithm to find Strongly Connected Components.
#    See https://www.geeksforgeeks.org/tarjan-algorithm-find-strongly-connected-components/
# 2. Can we use BFS instead of DFS in above algorithm?
#    See https://www.geeksforgeeks.org/check-given-directed-graph-strongly-connected-set-2-kosaraju-using-bfs/.

from graph_basics import Graph


def is_scc(graph):
    visited = [False] * len(graph.adj)
    graph.explore(0, visited)

    for node in range(len(graph.adj)):
        if not visited[node]:
            return False

    rev_adj = graph.reverse_graph()
    visited = [False] * len(rev_adj)
    graph.explore(0, visited, rev_adj)

    for node in range(len(graph.adj)):
        if not visited[node]:
            return False

    return True


def main():
    graph = Graph('d')
    print(is_scc(graph))


if __name__ == '__main__':
    main()
