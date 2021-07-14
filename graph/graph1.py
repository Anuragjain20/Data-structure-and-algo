class Graph:
    def  __init__(self,gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)  

    def bfs(self,vertex):
        visited = [vertex]
        queue = [vertex]
        while queue :
            deVertex = queue.pop(0)
            print(deVertex)
            for adjacentVertex in self.gdict[deVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)
                    queue.append(adjacentVertex)       

    def dfs(self,vertex):
        visited = [vertex]
        stack = [vertex]
        while stack:
            popVertex = stack.pop()
            print(popVertex)
            for adjacentVertex in self.gdict[popVertex]:
                if adjacentVertex not in visited:
                    visited.append(adjacentVertex)

                    stack.append(adjacentVertex)

    visited = []
    def dfsrec(self,vertex):
        if vertex  in self.visited:
            return
        else:
            self.visited.append(vertex)
            print(vertex)
            for  i in self.gdict[vertex][::-1]:
                self.dfsrec(i)    




    def topologicalSortUtil(self,v,visited,stack):
        visited.append(v)
        for i in self.gdict[v]:
            if  i not in visited:
                self.topologicalSortUtil(i,visited,stack)

        stack.insert(0,v) 

    def topologicalSort(self):
        visited = []
        stack = []
        for k in list(self.gdict):
            if k not in visited:
                self.topologicalSortUtil(k,visited,stack)

        print(stack) 
customDict = {"a":["b","c"],
            "b":["a","d","e"],
            "c":["a","e"],
            "d":["b","e","f"],
            "e":["d","f"],
            "f":["d","e"]}        

graph = Graph(customDict)
graph.addEdge("e","c")
print(graph.gdict)

graph.bfs("a")
print("------------------")
graph.dfs("a")
print("==================")
graph.dfsrec("a")
print("==================")
graph.topologicalSort()