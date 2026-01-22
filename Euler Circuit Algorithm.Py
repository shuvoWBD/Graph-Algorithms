# Python program to check whether a graph is
# Eulerian Path, Eulerian Circuit, or neither

# DFS to check connectivity, excluding zero-degree vertices
def dfs(node, adj, visited):
    visited[node] = True

    for neighbor in adj[node]:
        if not visited[neighbor]:
            dfs(neighbor, adj, visited)

# Function to check Eulerian Path or Circuit
def isEulerCircuit(v, adj):
    visited = [False] * v

    # Find first vertex with non-zero degree
    start = -1
    for i in range(v):
        if len(adj[i]) > 0:
            start = i
            break

    # No edges: graph is trivially Eulerian
    if start == -1:
        return 2

    # DFS from the first non-zero degree vertex
    dfs(start, adj, visited)

    # Check if all non-zero degree vertices are connected
    for i in range(v):
        if len(adj[i]) > 0 and not visited[i]:
            return 0  # Not connected

    # Count vertices with odd degree
    odd = 0
    for i in range(v):
        if len(adj[i]) % 2 != 0:
            odd += 1

    # Apply Eulerian rules
    if odd == 0:
        return 2 
    elif odd == 2:
        return 1 
    else:
        return 0 

if __name__ == "__main__":
    v = 5
    adj = [
        [1, 2, 3], 
        [0, 2], 
        [1, 0], 
        [0, 4], 
        [3]
    ]

    print(isEulerCircuit(v, adj))