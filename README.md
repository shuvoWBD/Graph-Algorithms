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




