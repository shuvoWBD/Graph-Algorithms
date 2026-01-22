# Recursive DFS function
def dfsRec(adj, visited, s, res):
    visited[s] = True
    res.append(s)

    # Recursively visit all unvisited neighbours
    for i in adj[s]:
        if not visited[i]:
            dfsRec(adj, visited, i, res)


# DFS for single connected component
def dfs(adj):
    visited = [False] * len(adj)
    res = []
    dfsRec(adj, visited, 0, res)
    return res


# Example graph (adjacency list)
adj = [
    [1, 2],
    [0, 3],
    [0, 3],
    [1, 2]
]

print(dfs(adj))
