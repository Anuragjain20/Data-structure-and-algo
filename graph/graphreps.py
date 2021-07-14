class Graph1:
    def __init__(self,gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def add_edge(self,vertex,edge):
        self.gdict[vertex].append(edge)
    def bfsutil(self,vertex,visited):
        
        queue = [vertex]
        while queue:
            n = queue.pop(0)
            print(n,end="--->")
            for i in self.gdict[n]:
                if i not in visited:
                    visited.append(i)
                    queue.append(i)          




    def bfs(self):
        visited = []
        for i in self.gdict:
            if i not in visited:
                visited.append(i)
                self.bfsutil(i,visited)
        print("\n")

customdict = {"a" : ["b","c","f"],
               "b":["a","c","d"], 
               "c": ["a","d"],
               "d":["a"],
               "e":["b","d"],
               "f":["a","b"]}
g1 = Graph1(customdict)
print("=============================")
print(g1.gdict)
g1.add_edge("a","e")
print("---------------------")
print(g1.gdict)
g1.bfs()


