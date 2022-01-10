# python 3

# prev would be 1 in case of root node
from collections import deque


def is_cycle_dfs(node, prev, adj, visited):
    visited[node] = True

    for i in adj[node]:
        if not visited[i]:
            if is_cycle_dfs(i, node, adj, visited):
                return True

        elif i != prev:
            return True

    return False


def is_cycle_bfs(root, adj, visited):
    queue = deque()

    queue.appendleft((root, -1))
    visited[root] = True

    while queue:
        node, prev = queue.pop()
        for i in adj[node]:
            if not visited[i]:
                visited[i] = True
                queue.appendleft((i, node))

            elif i != prev:
                return True

    return False
