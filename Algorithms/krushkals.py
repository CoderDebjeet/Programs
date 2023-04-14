def find(graph,node):
    if graph[node]<0:
        return node
    else:
        temp=find(graph,graph[node])
        graph[node]=temp
        return temp
def union(graph,a,b,answer):
    ta=a
    tb=b
    a=find(graph,a)
    b=find(graph,b)
    if a==b:              # if it gets loop then pass it
        pass
    else:
        answer.append([ta,tb])      
        if graph[a] < graph[b]:
            graph[a]=graph[a]+graph[b]
            graph[b]=a
        else:
            graph[b]=graph[a]+graph[b]
            graph[a]=b

#MAIN
n = int(input("Enter the number of nodes: "))
e=int(input("Enter the number of edges :"))
ipt= []
for i in range(e):
    u = int(input(f"Enter the first vertex of edge {i+1}: "))
    v = int(input(f"Enter the second vertex of edge {i+1}: "))
    d = int(input(f"Enter the distance between vertex {u} and vertex {v}: "))
    edge = [u, v, d]
    ipt.append(edge)
answer=[]
ipt=sorted(ipt,key=lambda ipt:ipt[2])
graph=[-1]*(n+1)
for u,v,d in ipt:
    union(graph,u,v,answer)
print("If you connect this edge you will get the desired graph:")
for item in answer:
    print(item)
    
