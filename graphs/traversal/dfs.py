# t.c. = O(N) + O(degree it will be = 2E)
# s.c. = O(2N) + Stackspace O(N) = O(3N) ~ O(N)

def dfs(node,adj,ans,visited):
    visited[node] = 1
    ans.append(node)

    for n in adj[node]:
        if visited[n] == 0:
            dfs(n,adj,ans,visited)
 
    return ans

n = 8 
adj_list= [
    [],
    [2,4],
    [1,3,6],
    [2],
    [1,5,7],
    [4,8],
    [2],
    [4,8],
    [5,7],
    ]
ans = []
visited = [0]*(n+1)
print(dfs(1,adj_list,ans,visited))