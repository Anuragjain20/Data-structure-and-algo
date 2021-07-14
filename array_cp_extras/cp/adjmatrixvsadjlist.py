from collections import defaultdict
graph = defaultdict(list)
v,e = map(int,input().split())
for i in range(e):
    u,v = map(str,input().split())
    graph[u].append(v)
    graph[v].append(u)
for  v in graph:
    print(v,graph[v])    
#SC = O(V)
#TC = O(V+E)
def dfs(graph,start,visited,path):
    path.append(start)
    visited[start] = True
    for neighbour in graph[start]: #O(V+E)
        if visited[neighbour] == False: #O(1)
            dfs(graph,neighbour,visited,path)
    return path        


path = []
start = 'A'
visited = defaultdict(bool)
traversedpath = dfs(graph,start,visited,path)
print(traversedpath)
"""
from collections import deque
from collections import defaultdict


'''
V E
FOR EVERY EDGE
U V
7 9
A B
A C 
A F
C E
C F
C D
D E 
D G
G F
'''
# T.C = O(V+)
# S.C = O(V)
def bfs(graph,start,visited,path):
    queue = deque()
    path.append(start)
    queue.append(start)
    visited[start] = True
    while len(queue) != 0:
        tmpnode = queue.popleft()
        for neighbour in graph[tmpnode]:
            if visited[neighbour] == False:
                path.append(neighbour)
                queue.append(neighbour)
                visited[neighbour] = True
    return path

graph = defaultdict(list)
v,e = map(int,input().split())
for i in range(e):
    u,v = map(str,input().split())
    graph[u].append(v)
    graph[v].append(u)

start = 'A'
path = []
visited = defaultdict(bool)
traversedpath = bfs(graph,start,visited,path)
print(traversedpath)
"""