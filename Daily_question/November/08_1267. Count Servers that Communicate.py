class Solution:
    def countServers(self, grid: list[list[int]]) -> int:
        r = len(grid)
        c = len(grid[0])
        # worng apprach 
        # ans = 0 
        # visited = [[False]*c for _ in range(r)]

        # def solve(row,col,visited):
        #     if row < 0 or row >= r or col < 0 or col >= c: 
        #         return 0 
        #     if visited[row][col]:
        #         return 0
        #     if grid[row][col] == 0 :
        #         return 0

        #     visited[row][col] = True 
        #     total_server = solve(row,col+1,visited) + solve(row,col-1,visited) + solve(row+1,col,visited) +solve(row-1,col,visited)
            
        #     return 1+total_server

        # for i in range(r):
        #     for j in range(c):
        #         if grid[i][j] == 1 and not visited[i][j] :
        #             val = solve(i,j,visited)
        #             ans += val

        # return ans 

        row = [0] * r 
        col = [0] * c
        count = 0

        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 :
                    row[i] += 1
                    col[j] += 1
        
        for i in range(r):
            for j in range(c):
                if grid[i][j] == 1 :
                    if row[i] > 1 or col[j] > 1:
                        count +=1
                    
        return count