def printmatrix(matrix):
    r,c = len(matrix),len(matrix[0])
    for i in range(r):
        for j in range(c):
            print(matrix[i][j],end=" ")
        print()

v,e = map(int,input().split())
matrix = [[0]*v for i in range(v)]
"""
for i in range(e):
    u,v = map(str,input().split())
    u = ord(u) - ord('A')
    v = ord(v) - ord('A')
    matrix[u][v] = 1
    matrix[v][u] = 1
"""
for i in range(e):
    u,v,w = map(str,input().split())
    u = ord(u) - ord('A')
    v = ord(v) - ord('A')
    matrix[u][v] = w
    matrix[v][u] = w

printmatrix(matrix)

