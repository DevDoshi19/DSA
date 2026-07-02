from collections import deque
from typing import List


class Solution:
    def numEnclaves(self, grid: List[List[int]]) -> int:
        m = len(grid)
        n = len(grid[0])
        visited = [[0 for _ in range(n)] for _ in range(m)]
        one = 0

        queue = deque()

        for i in range(m):
            if grid[i][0] == 1:
                queue.append((i,0))
                visited[i][0] = 1
            if grid[i][n-1] == 1 :
                visited[i][n-1] = 1
                queue.append((i,n-1))

        for j in range(n):
            if grid[0][j] == 1:
                queue.append((0,j))
                visited[0][j] = 1
            if grid[m-1][j] == 1 :
                visited[m-1][j] = 1
                queue.append((m-1,j))
                

        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        while queue:
            r,c = queue.popleft()

            for dr,dc in directions :
                nr,nc = r+dr , c+dc
                if 0<= nr < m and 0<=nc< n and grid[nr][nc] == 1 and visited[nr][nc] == 0 :
                    visited[nr][nc] = 1
                    queue.append((nr,nc))

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and visited[i][j] == 0:
                    one+=1
        
        return one
    

# t.c. whold be : O(m*n) + O(m*n*4) + O(m*n) = O(m*n)
# s.c. O(m*n) + O(m*n) = O(m*n)