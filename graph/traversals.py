# python 3
from collections import deque


def bfs(v, visited, adj, bfs_traversal):
    queue = deque()

    queue.appendleft(0)
    visited[0] = True

    while queue:
        node = queue.pop()
        bfs_traversal.append(node)

        for i in adj[node]:
            if not visited[i]:
                queue.appendleft(i)
                visited[i] = True


def dfs(node, visited, adj, dfs_traversal):
    visited[node] = True
    dfs_traversal.append(node)

    for i in adj[node]:
        if not visited[i]:
            dfs(i, visited, adj, dfs_traversal)


def components(v, adj):
    visited = [False for i in range(v)]
    dfs_traversal = []
    bfs_traversal = []

    for i in range(v):
        if not visited[i]:
            bfs(v, visited, adj, bfs_traversal)
            # or
            dfs(0, visited, adj, dfs_traversal)

