# python 3

# Find weakly connected components of directed graphs

"""
Example graphs input:
4
4
0 1
2 1
3 2
0 3

9
8
0 1
0 2
1 2
0 3
6 7
6 8
7 8
4 5
3 4

6
9
0 1 3
0 2 5
2 1 0
1 2 1
1 3 6
1 4 1
2 4 0
4 3 2
4 5 9
"""

# in bfs to set infinite distance use:
#  1. number of nodes + 1
#  2. number of edges + 1
#  3. special structure (tuple) with two values, one for distance and second a boolean stating distance
#     is infinite or not


from linked_list.reverse_linked_list import LinkedList
from collections import namedtuple, deque
from heapdict import heapdict


# Node_visit = namedtuple('Node_visit', ['previsit', 'postvisit'])


class Graph:
    def __init__(self, is_directed=None):
        self.adj = []
        edges = []
        num_vertices = int(input('Enter no. of vertices: '))
        num_edges = int(input('Enter no. of edges: '))
        print('Enter edges:')
        for i in range(num_edges):
            edge = list(map(int, input().split()))
            edges.append(edge)
        while True:
            if not is_directed:
                is_directed = input('Is graph Directed? (y/n): ')
            if is_directed == 'y' or is_directed == 'd':
                self.create_directed_graph_adj(edges, num_vertices)
                break
            elif is_directed == 'n' or is_directed == 'u':
                self.create_undirected_graph_adj(edges, num_vertices)
                break
            else:
                print('Try again')
                is_directed = None

    def create_directed_graph_adj(self, edges, vertices):
        adj = [[] for i in range(vertices)]

        # If graph is unweighted
        if len(edges[0]) == 2:
            for edge in edges:
                adj[edge[0]].append(edge[1])
            self.adj = adj
            return adj

        # If graph is weighted
        elif len(edges[0]) == 3:
            for edge in edges:
                adj[edge[0]].append([edge[1], edge[2]])
            self.adj = adj
            return adj

        else:
            raise ValueError('Edges contain values other 2 and 3')

    def create_undirected_graph_adj(self, edges, vertices):
        # adj = [LinkedList() for i in range(vertices + 1)]
        adj = [[] for i in range(vertices)]

        # if graph is unweighted
        if len(edges[0]) == 2:
            for edge in edges:     # edge = (u, v)
                u = edge[0]
                v = edge[1]
                # adj[u].push_back(v)
                # adj[v].push_back(u)
                adj[u].append(v)
                adj[v].append(u)
            self.adj = adj
            return adj

        # If graph is weighted
        elif len(edges[0]) == 3:
            for edge in edges:
                adj[edge[0]].append([edge[1], edge[2]])
                adj[edge[1]].append([edge[0], edge[2]])
            self.adj = adj
            return adj

        else:
            raise ValueError('Edges contain values other 2 and 3')

    def print_adj(self, adj=None):
        if not adj:
            adj = self.adj

        for node in range(len(adj)):
            print(node, ': ', end='')
            # adj[node].print_list()                  # If use linkedlist as adj list elements
            # print()
            print(adj[node])

    def reverse_graph(self, adj=None):
        if not adj:
            adj = self.adj

        adj_rev = [[] for i in range(len(adj))]

        for u in range(len(adj)):
            for v in adj[u]:
                adj_rev[v].append(u)

        return adj_rev

    # --------------------------------- Find connected components in undirected graph -------------------------------- #
    def explore(self, vertex, visited, adj):
        visited[vertex] = True
        for node in adj[vertex]:
            if not visited[node]:
                self.explore(node, visited, adj)

    def find_connected_components(self, adj=None):
        if not adj:
            adj = self.adj

        num_components = 0
        visited = [False for i in range(len(adj))]

        for node in range(len(adj)):
            if not visited[node]:
                self.explore(node, visited, adj)
                num_components += 1

        return num_components

    # -------------------------------------- Calculate pre and post visit numbers ------------------------------------ #
    def explore_pre_and_post(self, vertex, visited, visit_time, clock):
        visited[vertex] = True

        # previsit task
        visit_time[vertex].append(clock[0])
        clock[0] += 1

        for node in self.adj[vertex]:
            if not visited[node]:
                self.explore_pre_and_post(node, visited, visit_time, clock)

        # postvisit task
        visit_time[vertex].append(clock[0])
        clock[0] += 1

    def print_visit_time(self, visit_time):
        for node in range(len(visit_time)):
            print(node, ':', visit_time[node][0], '-', visit_time[node][1])

    def print_pre_and_post(self):
        visited = [False for i in range(len(self.adj))]
        visit_time = [[] for i in range(len(self.adj))]
        clock = [1]

        for node in range(len(self.adj)):
            if not visited[node]:
                self.explore_pre_and_post(node, visited, visit_time, clock)

        self.print_visit_time(visit_time)
        return visit_time

# -------------------------------------- Find strongly connected components naive way -------------------------------- #
    def explore_reachable(self, vertex, reachable, visited):
        visited[vertex] = True
        for node in self.adj[vertex]:
            if not visited[node]:
                visited[node] = True
                self.explore_reachable(node, reachable, visited)

        reachable.append(vertex)

    def find_reachable(self, vertex):
        reachable = []
        visited = [False for i in range(len(self.adj))]
        visited[vertex] = True

        for node in self.adj[vertex]:
            self.explore_reachable(node, reachable, visited)

        return reachable

    def find_num_of_strongly_connected_components_naive(self):
        reachable = [[] for i in range(len(self.adj))]
        for node in range(len(self.adj)):
            reachable[node] = self.find_reachable(node)

        strongly_connected_components = []
        visited = [False for i in range(len(self.adj))]

        for v in range(len(self.adj)):
            if visited[v]:
                continue
            component = [v]
            for u in reachable[v]:
                if not visited[u] and v in reachable[u]:
                    visited[u] = True
                    component.append(u)
            strongly_connected_components.append(component)

        return strongly_connected_components

    # -------------------------------------- Find strongly connected components -------------------------------------- #
    def explore_dfs(self, vertex, adj, visited, post_list):
        visited[vertex] = True
        for node in adj[vertex]:
            if not visited[node]:
                self.explore_dfs(node, adj, visited, post_list)

        post_list.append(vertex)

    def dfs(self, adj, visited, post_list):
        for node in range(len(adj)):
            if not visited[node]:
                self.explore_dfs(node, adj, visited, post_list)

    def explore_scc(self, vertex, visited, curr_scc):
        visited[vertex] = True
        for node in self.adj[vertex]:
            if not visited[node]:
                self.explore_scc(node, visited, curr_scc)

        curr_scc.append(vertex)

    def find_strongly_connected_components(self):
        adj_rev = self.reverse_graph()

        # Creating DFS traversal list according to post numbers
        visited = [False] * len(self.adj)
        post_list = []
        self.dfs(adj_rev, visited, post_list)

        visited = [False] * len(self.adj)
        scc_arr = []

        for node in reversed(post_list):
            curr_scc = []
            if not visited[node]:
                self.explore_scc(node, visited, curr_scc)
                scc_arr.append(curr_scc)

        return scc_arr

    # ------------------------------------------- Topological sort naive way ---------------------------------------- #
    def is_empty(self, removed):
        for node in range(len(self.adj)):
            if not removed[node]:
                return False
        return True

    def is_sink(self, vertex, removed):
        if not self.adj[vertex]:
            return True

        for node in self.adj[vertex]:
            if not removed[node]:
                return False
        return True

    def find_sink(self, vertex, removed):
        if not self.is_sink(vertex, removed):
            for node in self.adj[vertex]:
                if not removed[node]:
                    return self.find_sink(node, removed)
        else:
            return vertex

    # Topological sort or linear order
    def topo_sort_naive(self):
        removed = [False] * len(self.adj)
        topo_sort_arr = []

        while not self.is_empty(removed):
            sink = self.find_sink(0, removed)
            topo_sort_arr.append(sink)
            removed[sink] = True

        return topo_sort_arr

    # -------------------------------------------------- Topological sort -------------------------------------------- #
    # Try topological sorting using kahn's algorithm.....topo sort using indegree
    def explore_topo(self, vertex, visited, topo_sort_arr):
        visited[vertex] = True
        for node in self.adj[vertex]:
            if not visited[node]:
                self.explore_topo(node, visited, topo_sort_arr)
        topo_sort_arr.append(vertex)

    def topo_sort(self):
        visited = [False] * len(self.adj)
        topo_sort_arr = []
        for node in range(len(self.adj)):
            if not visited[node]:
                self.explore_topo(node, visited, topo_sort_arr)

        return topo_sort_arr

    # ---------------------------------------------- Find shortest path BFS ------------------------------------------ #
    def reconstruct_path(self, prev, source, end):
        path = []
        while end is not None:
            path.append(end)
            end = prev[end]

        return list(reversed(path))

    def find_shortest_path(self, source, end, adj=None):
        if not adj:
            adj = self.adj

        # Taking infinite distance as num_vertices + 1
        inf = len(adj) + 1

        # initializing dist and prev arrays
        dist = [inf] * len(adj)
        dist[source] = 0
        prev = [None] * len(adj)

        # Initializing queue
        queue = deque()
        queue.appendleft(source)

        while queue:
            u = queue.pop()
            for v in adj[u]:
                if dist[v] == inf:
                    queue.appendleft(v)
                    dist[v] = dist[u] + 1
                    prev[v] = u

        return self.reconstruct_path(prev, source, end)

    # -------------------------------------- Find shortest path using naive way -------------------------------------- #
    def relax_edge(self, u, v, weight_uv, dist, prev, adj=None):
        if not adj:
            adj = self.adj

        # Reducing distance if edge can be relaxed
        if dist[v] > dist[u] + weight_uv:
            dist[v] = dist[u] + weight_uv
            prev[v] = u
            return True
        return False

    def find_fastest_route_naive(self, source, adj=None):
        if not adj:
            adj = self.adj

        # Return if not a weighted graph
        for node in range(len(adj)):
            if not adj[node]:
                continue

            if isinstance(adj[node][0], int):
                return 'Provided graph is not weighted'
            else:
                break

        # Main functionality
        # Initializing inf as float('inf')
        inf = float('inf')

        # Initializing dist and prev arrays
        dist = [inf] * len(adj)
        dist[source] = 0
        prev = [None] * len(adj)

        while True:
            relaxed_in_iteration = False
            for u in range(len(adj)):
                for v in adj[u]:
                    # v[0] - adjacent node        v[1] - weight of adjacent node
                    is_relaxed = self.relax_edge(u, v[0], v[1], dist, prev, adj)
                    if is_relaxed:
                        relaxed_in_iteration = True

            if not relaxed_in_iteration:
                break

        return dist

    # ------------------------------------ Shortest Path using Dijkstra's algorithm ---------------------------------- #
    def find_fastest_route_dijkstra(self, source, adj=None):
        # Time complexity = (V + E)log(V)
        if not adj:
            adj = self.adj

        # Return if not a weighted graph
        for node in range(len(adj)):
            if not adj[node]:
                continue

            if isinstance(adj[node][0], int):
                return 'Provided graph is not weighted'
            else:
                break

        # Main functionality
        # Initializing inf as float('inf')
        inf = float('inf')

        # Initializing dist and prev arrays
        dist = [inf] * len(adj)
        dist[source] = 0
        prev = [None] * len(adj)

        # Initializing priority queue/Min heap
        heap = heapdict()
        for node in range(len(adj)):
            heap[node] = inf
        heap[source] = 0

        while heap:
            u = heap.popitem()[0]        # return (key, value) as (node, dist) so, popitem()[0]
            for v, weight_uv in adj[u]:
                # relax all the neighbouring edges of u
                if dist[v] > dist[u] + weight_uv:
                    dist[v] = dist[u] + weight_uv
                    prev[v] = u
                    heap[v] = dist[v]

        return dist

    # write bellman ford algo
    # find negative cycles i.e. print nodes of negative cycles
    # reconstruct path to find infinite arbitrage from source to some node t including negative cycle


def main():
    graph = Graph()

    # print adjacency list of graph
    graph.print_adj()

    # Functions on graph
    # visited = [False for i in range(num_vertices+1)]
    # graph.explore(1, visited)
    # print(graph.topo_sort_naive())
    # print(graph.topo_sort())

    # print(graph.find_connected_components())
    # graph.print_pre_and_post()
    # print(graph.find_num_of_strongly_connected_components())
    # print(graph.find_strongly_connected_components())
    # print(graph.find_shortest_path(0, 5))
    # print(graph.find_fastest_route_naive(0))
    print(graph.find_fastest_route_dijkstra(0))


if __name__ == '__main__':
    main()
