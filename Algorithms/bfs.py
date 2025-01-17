from collections import deque

sz = 1000
inf = 1e9

class Node:
    def __init__(self):
        self.parent = -1
        self.distance = inf
        self.color = "WHITE"

adj = [[] for _ in range(sz+1)]
nodes = [Node() for _ in range(sz+1)]

def BFS(src):
    global nodes, adj
    for i in range(1, n+1):
        nodes[i].color = "WHITE"
        nodes[i].distance = inf
        nodes[i].parent = -1
    nodes[src].color = "GRAY"
    nodes[src].distance = 0

    Q = deque()
    Q.append(src)

    while Q:
        u = Q.popleft()
        for v in adj[u]:
            if nodes[v].color == "WHITE":
                nodes[v].color = "GRAY"
                nodes[v].distance = nodes[u].distance + 1
                nodes[v].parent = u
                Q.append(v)
        nodes[u].color = "BLACK"
start=int(input("Enter the starting point :- "))
end=int(input("Enter the end vertex :- "))
def printPath(v):
    src = start
    if v == src:
        print(src)
    elif nodes[v].parent == -1:
        print("There is no path.")
    else:
        path = []
        while True:
            path.append(v)
            if v == src:
                break
            v = nodes[v].parent
        path.reverse()
        print(*path)

n, m = map(int, input("Enter no of vetex and edges : ").split())

for i in range(m):
    u, v = map(int, input("Enter vertex1 vertex 2 of the edge : ").split())
    adj[u].append(v)
    adj[v].append(u)

BFS(start) # 1-indexed

for i in range(1, n+1):
    print(f"node {i}: Distance={nodes[i].distance}, Parent={nodes[i].parent}, Color={nodes[i].color}")

printPath(end)
