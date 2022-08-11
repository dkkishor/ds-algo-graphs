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
    global parent
    global hascycle

    q = deque()

    # Add the first/start node to the queue
    q.append(source)
    visited[source] = 1

    while q:
        node = q.popleft()

        for neighbor in adjlist[node]:
            if visited[neighbor] == -1:  # Tree Edge
                q.append(neighbor)
                visited[neighbor] = 1
                parent[neighbor] = node  # TO detect cycles (Cross Edge)
            else:  # Neighbor has been visited
                if neighbor != parent[node]:
                    hascycle = True  # Detected a cycle (Cross Edge)
                    # return True  # you can return from here if the objective is to just detect the cycle
    # return False  # you can return from here if the objective is to just detect the cycle


def dfs(node):
    global adjlist
    global visited
    global parent
    global hascycle

    visited[node] = 1
    for neighbor in adjlist[node]:
        if visited[neighbor] == -1:  # Tree Edge
            parent[neighbor] = node  # TO detect cycles (Cross Edge)
            dfs(neighbor)
            # if dfs(neighbor): return True  # you can return from here if the objective is to just detect the cycle
        else:  # Neighbor has been visited
            if neighbor != parent.get(node):
                hascycle = True  # Detected a cycle (Back Edge)
                # return True  # you can return from here if the objective is to just detect the cycle

    # return False  # you can return from here if the objective is to just detect the cycle


# Outerloop
def graph(n, edges, bfsflag=True):
    global adjlist
    global visited
    global parent
    global hascycle

    components = 0

    adjlist = [[] for i in range(n)]
    visited = [-1 for i in range(n)]
    parent  = {}
    hascycle = False

    # Build the graph
    build(n, edges)

    for v in range(n): # 0 to n-1
        if visited[v] == -1:
            components += 1
            bfs(v) if bfsflag else dfs(v)

    print(str(components) + (" (bfs)" if bfsflag else " (dfs)") + ", hascycle: " + str(hascycle))
    return components


if __name__ == "__main__":
    graph(5, [[0,1],[1,2],[3,4]])
    graph(5, [[0,1],[1,2],[2,3],[3,4]], False)
    graph(6, [[0, 1], [0, 2], [2, 3], [2, 4], [1,5], [4,5]])
    graph(6, [[0, 1], [0, 2], [2, 3], [2, 4], [1, 5], [4, 5]], False)


'''
OUTPUT:
2 (bfs), hascycle: False
1 (dfs), hascycle: False
1 (bfs), hascycle: True
1 (dfs), hascycle: True
'''