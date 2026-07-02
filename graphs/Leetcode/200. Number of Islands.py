from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        
        def dfs(i,j):
            if i<0 or i >= m or j < 0 or j >= n :
                return 

            if grid[i][j] == "0" :
                return 

            grid[i][j] = "0" 
            dfs(i-1,j)
            dfs(i+1,j)
            dfs(i,j-1)
            dfs(i,j+1)
        
        m = len(grid)
        n = len(grid[0])
        islands = 0

        for i in range(m):
            for j in range(n) :
                if grid[i][j] == "1" :
                    dfs(i,j)
                    islands += 1 

        return islands
    