# Graph-Algorithms

A **Graph Algorithm** is a set of computational steps used to solve problems related to graphs, which consist of vertices (nodes) and edges (connections). These algorithms are used to explore graphs, find shortest paths, detect cycles, build minimum spanning trees, and analyze connectivity. Common applications include networking, routing, social networks, and scheduling problems.



**BFS**
---------------------------------------------------------
Breadth First Search (BFS) is a graph traversal algorithm that starts from a source node and explores the graph level by level. First, it visits all nodes directly adjacent to the source. Then, it moves on to visit the adjacent nodes of those nodes, and this process continues until all reachable nodes are visited.


**Steps**
  1. Start with a graph represented as an adjacency list.

  2. Create a visited array and mark all vertices as unvisited.

  3. Choose a source vertex and mark it as visited.

  4. Insert the source vertex into a queue.

  5. While the queue is not empty:

       * Remove the front vertex from the queue.

       * Add it to the result list.

       * For each adjacent vertex of the removed vertex:

       *  If it is not visited, mark it as visited and insert it into the queue.

6. Repeat until the queue becomes empty.

7. The result list contains the BFS traversal order.


**Time Complexity**

 O(V + E), BFS explores all the vertices and edges in the graph. It visits every vertex and edge only once.



 **DFS**
 -----------------------------------------------

Depth First Search (DFS) is a graph traversal method that starts from a source vertex and explores each path completely before backtracking and exploring other paths. 


**Steps**

  1. Represent the graph using an adjacency list.

  2. Create a visited array and mark all vertices as unvisited.

  3. Create an empty list to store the DFS traversal result.

  4. Start DFS from the source vertex (vertex 0).

  5. Mark the current vertex as visited and add it to the result list.

  6. For each adjacent vertex of the current vertex:

       * If it is not visited, recursively call DFS on that vertex.

  7. Continue the process until all reachable vertices are visited.

  8. The result list contains the DFS traversal order.


**Time complexity:**

O(V + E), where V is the number of vertices and E is the number of edges in the graph.



**Prim’s Algorithm**
----------------------------------------------------
This algorithm always starts with a single node and moves through several adjacent nodes, in order to explore all of the connected edges along the way.

 * The algorithm starts with an empty spanning tree.

 * The idea is to maintain two sets of vertices. The first set contains the vertices already included in the MST, and the other set contains the vertices not yet included.

 * At every step, it considers all the edges that connect the two sets and picks the minimum weight edge from these edges. After picking the edge, it moves the other endpoint of the edge to the set containing MST.


**Steps**

  1. Determine an arbitrary vertex as the starting vertex of the MST. We pick 0 in the above diagram.

  2. Follow steps 3 to 5 till there are vertices that are not included in the MST.

  3. Find edges connecting any tree vertex with the fringe vertices.

  4. Find the minimum among these edges.

  5. Add the chosen edge to the MST. Since we consider only the edges that connect fringe vertices with the rest, we never get a cycle.

  6. Return the MST and exit.



**Kruskal’s Algorithm**
--------------------------------------------

A minimum spanning tree (MST) or minimum weight spanning tree for a weighted, connected, and undirected graph is a spanning tree that has minimum weight. The weight of a spanning tree is the sum of all edges in the tree.  


**Steps**

 1. Sort all the edges in a non-decreasing order of their weight.

 2. Pick the smallest edge. Check if it forms a cycle with the spanning tree formed so far. If the cycle is not formed, include this edge. Else, discard it.  It       uses the Disjoint Sets to detect cycles.

 3. Repeat step 2 until there are (V-1) edges in the spanning tree.


**Time Complexity**

 O(E * log E) or O(E * log V) 



**Dijkstra's Algorithm**
-----------------------------------------------
Dijkstra’s Algorithm is a graph algorithm used to find the shortest path from a single source vertex to all other vertices in a weighted graph with non-negative edge weights. It works by repeatedly selecting the unvisited vertex with the smallest known distance, updating the distances of its neighboring vertices, and marking the vertex as visited. This process continues until the shortest distances to all vertices are determined.


**Steps**

  1. Represent the graph as an adjacency list with weights on edges.

  2. Initialize a distance array where the distance to all vertices is set to infinity.

 3. Set the distance of the source vertex to 0.

 4. Insert the source vertex into a priority queue (min-heap).

5. While the priority queue is not empty:

     * Remove the vertex with the minimum distance.

     * If the extracted distance is greater than the stored distance, skip it.

     * For each neighboring vertex:

           * Calculate the new distance through the current vertex.

           * If the new distance is smaller, update the distance and push it into the queue.

6. Repeat until all reachable vertices are processed.

7. The distance array now contains the shortest distances from the source to all vertices.


**Time Complexity**

 O((V+E)*logV), Where E is the number of edges and V is the number of vertices.



 **Euler Circuit Algorithm**
 ----------------------------------------------------------------
 An Euler Circuit Algorithm is used to determine and construct a path in a graph that starts and ends at the same vertex while visiting every edge exactly once.


 **Key Conditions**

    * The graph must be connected.

    * Every vertex must have an even degree.


**Steps**

   1. Create the graph using an adjacency list and maintain an array to store the in-degree of each vertex.

   2. Check strong connectivity:

          * Perform DFS on the original graph starting from a vertex with non-zero degree.

          * Perform DFS on the transpose (reversed) graph.

          * If all vertices with edges are visited in both cases, the graph is strongly connected.

   3. Check degree condition:

          * For every vertex, verify that its in-degree is equal to its out-degree.

   4. Decide Eulerian cycle:

          * If the graph is strongly connected and every vertex has equal in-degree and out-degree, then the graph has an Euler circuit.

          * Otherwise, it does not have an Euler circuit.

   5. Output the result based on the checks.


**Time complexity**

   O(V + E)



**Johnson’s Algorithm**
-------------------------------------------------------------
Johnson’s Algorithm is a graph algorithm used to find the shortest paths between all pairs of vertices in a weighted, directed graph that may contain negative edge weights, but no negative weight cycles.


**Steps**

  1. et the given graph be G. Add a new vertex s to the graph, add edges from the new vertex to all vertices of G. Let the modified graph be G'.

  2. Run the Bellman-Ford algorithm on G' with s as the source. Let the distances calculated by Bellman-Ford be h[0], h[1], .. h[V-1]. If we find a negative           weight cycle, then return. Note that the negative weight cycle cannot be created by new vertex s as there is no edge to s. All edges are from s.

  3. Reweight the edges of the original graph. For each edge (u, v), assign the new weight as "original weight + h[u] - h[v]".

  4. Remove the added vertex s and run Dijkstra's algorithm for every vertex.


**Time Complexity**

  O(V2log V + VE). 



**Bridge Finding Algorithm**
--------------------------------------------------------------------------
A Bridge Finding Algorithm is used to identify bridges in a graph.


**Steps**

   1. **Initialization:**

          * Mark all vertices as unvisited.

          * Create arrays: disc[] (discovery time), low[] (lowest reachable ancestor), and parent[].

   2. **Depth-First Search (DFS):**

          * Start DFS from any unvisited vertex.

          * For each adjacent vertex v of u:

                     * If v is unvisited, recursively DFS on v.

                     * Update low[u] = min(low[u], low[v]).

  3. **Bridge Detection:**

         * fter visiting v, if low[v] > disc[u], edge (u, v) is a bridge.

  4. **Back Edge Handling:**

        * If v is visited and not the parent of u, update low[u] = min(low[u], disc[v]).
    
  5. **Repeat:**
        * Continue DFS until all vertices are visited.
    
        * All edges satisfying the bridge condition are reported.


  **Time Complexity**

     O(V+E)



**Reverse Delete Algorithm**
---------------------------------------------------
he Reverse Delete Algorithm is a graph algorithm used to find a Minimum Spanning Tree (MST) of a connected, weighted, undirected graph.


**Steps**

   1. Sort all edges of the graph in decreasing order of weight.

   2. Start with the full graph containing all edges.

   3. Pick the edge with the highest weight.

   4. Remove this edge if the graph remains connected.

   5. If removing the edge disconnects the graph, keep it.

    6. Repeat until no more edges can be removed.

    7. The remaining edges form the Minimum Spanning Tree.


  **Time complexity**

    O((E*(V+E)) + E log E) where E is the number of edges.



**Shortest Path Faster Algorithm**
-----------------------------------------------------
The Shortest Path Faster Algorithm (SPFA) is an improved version of the Bellman–Ford Algorithm used to find the shortest paths from a single source to all other vertices in a weighted graph, even when negative edge weights are present.


**Steps**

   1. Create an array d[] to store the shortest distance of all vertex from the source vertex. Initialize this array by infinity except for d[S] = 0 where S is          the source vertex.

   2. Create a queue Q and push starting source vertex in it.

          * while Queue is not empty, do the following for each edge(u, v) in the graph.

                          * If d[v] > d[u] + weight of edge(u, v).

                           * d[v] = d[u] + weight of edge(u, v).

                            * If vertex v is not present in Queue, then push the vertex v into the Queue.


**Time Complexity**

     * **Average Time Complexity:** O(|E|) 

     * **Worstcase Time Complexity:** O(|V|.|E|) 



**Iterative Deepening Search**
-------------------------------------------------------
Iterative Deepening Search (IDS) is a graph and tree search algorithm that combines the space efficiency of DFS with the completeness of BFS. It works by repeatedly applying Depth-Limited Search (DLS) with increasing depth limits until the goal is found.


**Steps**

  1. Start IDDFS:

          * The algorithm begins with depth limit = 0

          * It calls Depth-Limited Search (DLS) using this limit.

2. Call DLS:

        * if src == target, the search is successful and returns true.

        * If the depth limit becomes 0, the search stops and returns false.

        * Otherwise, the algorithm explores all adjacent nodes of src.

        * For each adjacent node, DLS is called again with limit - 1.

3. Increase Depth Limit:

        * If the target is not found at the current depth.

        * IDDFS increases the depth limit by 1.

        * DLS is called again from the source node.

4. Repeat the Process:

        * This process continues until:

                      * The target is found → return true.

                      * The depth limit reaches max_depth → stop searching.



**Floyd Warshall Algorithm**
--------------------------------------------------
The Floyd–Warshall Algorithm is used to find the shortest paths between all pairs of vertices in a weighted graph.

It works for:

     * Directed or undirected graphs.

     * Graphs with negative edge weights.

     * But no negative weight cycles.


**Steps**

    1. Start by updating the distance matrix by treating each vertex as a possible intermediate node between all pairs of vertices.

    2. Iterate through each vertex, one at a time. For each selected vertex k, attempt to improve the shortest paths that pass through it.

    3. When we pick vertex number k as an intermediate vertex, we already have considered vertices {0, 1, 2, .. k-1} as intermediate vertices. 

    4. For every pair (i, j) of the source and destination vertices respectively, there are two possible cases.

                 * k is not an intermediate vertex in shortest path from i to j. We keep the value of dist[i][j] as it is. 

                 * k is an intermediate vertex in shortest path from i to j. We update the value of dist[i][j] as dist[i][k] + dist[k][j], if dist[i][j] > dist[i]                      [k] + dist[k][j].

    5. Repeat this process for each vertex k until all intermediate possibilities have been considered.

6. Final Decision:

        * If the target is found at any depth ≤ max_depth, IDDFS returns true.

        * If the target is not found after all depth levels, IDDFS returns false.


**Time Complexity**

   O(V3), where V is the number of vertices in the graph and we run three nested loops each of size V.
