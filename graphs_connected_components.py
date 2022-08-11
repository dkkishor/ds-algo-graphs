'''
General Structure of a graph problem is

1) Build the Graph
2) BFS / DFS Traversal
3) Outer Loop

Input is
1) Number of vertices, n=5,
2) list of edges [[0,1],[1,2],[3,4]]

Output:
Number of connected components
'''

from collections import deque

adjlist = []
visited = []

def build(n, edges):
    # Initialize adjacency List
    global adjlist

    for (src, dst) in edges:
        adjlist[src].append(dst)
        adjlist[dst].append(src) # Undirected

def bfs(source):
    global adjlist
    global visited

    q = deque()

    # Add the first/start node to the queue
    q.append(source)
    visited[source] = 1

    while q:
        node = q.popleft()

        for neighbor in adjlist[node]:
            if visited[neighbor] == -1:
                q.append(neighbor)
                visited[neighbor] = 1


def dfs(node):
    global adjlist
    global visited

    visited[node] = 1
    for neighbor in adjlist[node]:
        if visited[neighbor] == -1:
            dfs(neighbor)


# Outerloop
def graph(n, edges, bfsflag=True):
    global adjlist
    global visited
    components = 0

    adjlist = [[] for i in range(n)]
    visited = [-1 for i in range(n)]

    # Build the graph
    build(n, edges)

    for v in range(n): # 0 to n-1
        if visited[v] == -1:
            components += 1
            bfs(v) if bfsflag else dfs(v)

    print(str(components) + (" (bfs)" if bfsflag else " (dfs)"))
    return components


if __name__ == "__main__":
    graph(5, [[0,1],[1,2],[3,4]])
    graph(5, [[0,1],[1,2],[2,3],[3,4]], False)


'''
OUTPUT:
2 (bfs)
1 (dfs)
'''
