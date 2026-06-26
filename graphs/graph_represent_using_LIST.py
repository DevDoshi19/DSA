n = 5
m = 6

## Time complexity whould be O(2E)

edges = [[1,2],[1,3],[2,4],[3,4],[3,5],[4,5]]
lst = [[] for i in range(n+1)]

for u,v in edges :
    lst[u].append(v)
    lst[v].append(u)

print(lst)