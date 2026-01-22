import heapq
import sys

def dijkstra(adj, src):
    V = len(adj)

    # Min-heap (priority queue)
    pq = []

    # Distance array
    dist = [sys.maxsize] * V

    # Distance of source is 0
    dist[src] = 0
    heapq.heappush(pq, (0, src))

    while pq:
        d, u = heapq.heappop(pq)

        # Skip if not the shortest distance
        if d > dist[u]:
            continue

        # Relax edges
        for v, w in adj[u]:
            if dist[u] + w < dist[v]:
                dist[v] = dist[u] + w
                heapq.heappush(pq, (dist[v], v))

    return dist


# Example graph (adjacency list with weights)
adj = [
    [(1, 4), (2, 1)],
    [(3, 1)],
    [(1, 2), (3, 5)],
    []
]

src = 0
print(dijkstra(adj, src))
