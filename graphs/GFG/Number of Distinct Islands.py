class Solution:
    def countDistinctIslands(self, grid):
        # code here
        
        m = len(grid)
        n = len(grid[0])
        
        dis = set()
        
        visited = [[0 for _ in range(n)] for _ in range(m)]
        
        def dfs(i, j, base_i, base_j, ans):
            if i < 0 or i >= m or j<0 or j >= n or grid[i][j] == "W" or visited[i][j] == 1:
                return 
            
            visited[i][j] = 1 
            
            ans.append((i - base_i, j - base_j))
            
            dfs(i,j+1,base_i, base_j, ans)
            dfs(i+1,j,base_i, base_j, ans)
            dfs(i,j-1,base_i, base_j, ans)
            dfs(i-1,j,base_i, base_j, ans)
        
        
        for i in range(m):
            for j in range(n):
                if grid[i][j]=="L" and visited[i][j] == 0 :
                    ans = []
                    dfs(i,j,i,j,ans)
                    dis.add(tuple(ans))
        
        return len(dis)