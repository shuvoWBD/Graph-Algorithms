from collections import deque

# BFS for single connected component
def bfs(adj):
    V = len(adj)
    visited = [False] * V
    res = []

    src = 0
    q = deque()
    visited[src] = True
    q.append(src)

    while q:
        curr = q.popleft()
        res.append(curr)

        # visit all unvisited neighbours
        for x in adj[curr]:
            if not visited[x]:
                visited[x] = True
                q.append(x)

    return res


# Example graph (adjacency list)
adj = [
    [1, 2],
    [0, 3],
    [0, 3],
    [1, 2]
]

print(bfs(adj))
