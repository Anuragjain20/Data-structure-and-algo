class Graph:
    def  __init__(self,gdict = None):
        if gdict is None:
            gdict = {}
        self.gdict = gdict

    def addEdge(self,vertex,edge):
        self.gdict[vertex].append(edge)  

    def bfs(self,start,end):
        queue = []
        queue.append([start])
        while queue:
            path = queue.pop(0)
            node = path[-1] 
            if  node == end:
                return path
            for adjacent in self.gdict.get(node,[]):
                new_path = list(path)
                new_path.append(adjacent)     
                queue.append(new_path)

customDict = {"a":["b","c"],"b":["d","g","c"],"c":["d","e"],"d":["f"],"e":["f"],"g":["f"]}                
g = Graph(customDict)
print(g.bfs("b","e"))