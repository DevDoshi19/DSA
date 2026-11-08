class Solution:
    def uniquePathsIII(self, grid: list[list[int]]) -> int:
        r=len(grid)
        c=len(grid[0])
        visited = [[False]*c for _ in range(r)]

        opstacles = 0
        for i in range(r):
            for j in range(c):
                if grid[i][j] == -1:
                    opstacles += 1 

        need_moves = (r*c)-opstacles
        ans = 0
        def backtrack(row,col,curr_move):
            if row < 0 or row >= r or col < 0 or col >= c :
                return 0 
            
            if visited[row][col] is True :
                return 0 
            
            if grid[row][col] == -1 :
                return 0

            if grid[row][col] == 2 :
                if curr_move == need_moves:
                    return 1 
                return 0 

            visited[row][col] = True 
            goal = (backtrack(row,col+1,curr_move+1) + 
            backtrack(row,col-1,curr_move+1) +
            backtrack(row+1,col,curr_move+1) + 
            backtrack(row-1,col,curr_move+1))
            visited[row][col] = False 

            return goal

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1:
                    temp = backtrack(i,j,1)
                    ans += temp 

        return ans