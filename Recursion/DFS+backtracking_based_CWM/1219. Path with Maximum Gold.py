class Solution:
    def getMaximumGold(self, grid: list[list[int]]) -> int:
        r = len(grid)
        c = len(grid[0])

        visited = [[False for _ in range(c)] for _ in range(r)]
        self.maxi = float("-inf")

        def dfs(grid,row,col,visited):
            if row < 0 or row >= r or col <0 or col >= c:
                return 0 
            if grid[row][col] == 0 :
                return 0 
            
            if visited[row][col]:
                return 0 
            
            visited[row][col] = True
            total = max(dfs(grid,row,col+1,visited) 
                    ,dfs(grid,row,col-1,visited) 
                    ,dfs(grid,row+1,col,visited)
                    ,dfs(grid,row-1,col,visited))

            visited[row][col] = False
            return grid[row][col] + total

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 0:
                    continue
                total = dfs(grid,i,j,visited)
                self.maxi = max(self.maxi,total)

        return self.maxi if self.maxi != float("-inf") else 0
    
# the t.c. = O(R*C * 3*L) where R is the number of rows, C is the number of columns, and L is the length of the word. The 3^L factor arises because from each cell, we can explore up to 3 directions (excluding the direction we came from) for each character in the word.
# the s.c. = O(R*C) for the visited array and O(L) for the recursion stack, where L is the length of the word.