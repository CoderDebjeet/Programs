from heapq import *
def prims(graph,start,parent,distance,visited):
    bag=[]     #possibilites which can be choose in future
    heappush(bag, [0,start])
    distance[start]=0
    parent[start]=-1
    while bag:
        d,n=heappop(bag)  #node pe pohoch gya
        if not visited[n]: # if not visited 
            visited[n]=1   #then visit
            for cd,cn in graph[n]:     #cn=old dist cd=newdist
                if distance[cn]>cd and not visited[cn]:
                    parent[cn]=n      #update parent
                    distance[cn]=cd        #update dist
                    heappush(bag, [cd,cn])
    print("distance:vertex")
    print(distance)
    print("child:parent")
    print(parent)


n = int(input("Enter the number of vertices: "))
e = int(input("Enter the number of edges: "))
graph={}
parent={}
distance={}
visited={}
for i in range(1,n+1):
    graph[i]=[]
    parent[i]=None
    distance[i]=10**8+1
    visited[i]=0
print("Enter the edges in the format 'vertex1 vertex2 dist':")
for _ in range(e):
    u, v, d = map(int, input().split())
    graph[u].append([d,v])
    graph[v].append([d,u])
start=1
prims(graph, start, parent, distance, visited)