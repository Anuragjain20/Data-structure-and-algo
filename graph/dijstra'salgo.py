from collections import defaultdict



class Graph:
    def __init__(self):
        self.nodes =  set()
        self.edges = defaultdict(list)
        self.distances = {}

    def addNode(self,value):
        self.nodes.add(value)

    def addEdge(self,FromNode,ToNode,distance):
        self.edges[FromNode].append(ToNode)
        self.distances[(FromNode,ToNode)] = distance

def dijkstra(graph,initial):
    visited = {initial : 0}
    path = defaultdict(list)
    node = set(graph.nodes)
    while node:
        minNode = None
        for n in node:
            if n in visited:
                if minNode == None:
                    minNode = n
                elif visited[n] < visited[minNode]:
                    minNode = n
        if minNode is None:
            break
        node.remove(minNode)
        currweight = visited[minNode]
        for edge in graph.edges[minNode]:
            weight = currweight + graph.distances[(minNode,edge)]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(minNode) 

    return visited ,path







customGraph = Graph()
customGraph.addNode("A")
customGraph.addNode("B")
customGraph.addNode("C")
customGraph.addNode("D")
customGraph.addNode("E")
customGraph.addNode("F")
customGraph.addNode("G")
customGraph.addEdge("A", "B", 2)
customGraph.addEdge("A", "C", 5)
customGraph.addEdge("B", "C", 6)
customGraph.addEdge("B", "D", 1)
customGraph.addEdge("B", "E", 3)
customGraph.addEdge("C", "F", 8)
customGraph.addEdge("D", "E", 4)
customGraph.addEdge("E", "G", 9)
customGraph.addEdge("F", "G", 7)


print(dijkstra(customGraph, "A"))    





                