n = 5
m = 6

edges = [[1,2],[1,3],[2,4],[3,4],[3,5],[4,5]]

## Time complexity whould be O(n x n)

matrix = [[0 for _ in range(n+1)] for _ in range(n+1)]

r = len(edges)
c = len(edges[0])

for u,v in edges:
    matrix[u][v] = 1 
    matrix[v][u] = 1 
    

print(matrix)

