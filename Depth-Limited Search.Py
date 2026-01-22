# Depth Limited Search (DLS) implementation in Python

def depth_limited_search(node, goal, graph, limit, visited=None):
    if visited is None:
        visited = set()

    # Goal test
    if node == goal:
        return node

    # Depth limit reached
    if limit == 0:
        return "cutoff"

    visited.add(node)
    cutoff_occurred = False

    # Expand node (visit children)
    for child in graph.get(node, []):
        if child not in visited:
            result = depth_limited_search(child, goal, graph, limit - 1, visited)

            if result == "cutoff":
                cutoff_occurred = True
            elif result != "failure":
                return result

    return "cutoff" if cutoff_occurred else "failure"


# ---------------- Example Usage ----------------

# Graph representation (adjacency list)
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['G'],
    'F': [],
    'G': []
}

start_node = 'A'
goal_node = 'G'
depth_limit = 3

result = depth_limited_search(start_node, goal_node, graph, depth_limit)

print("Result:", result)
