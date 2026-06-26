from typing import List
from collections import deque
class Solution:
    def updateMatrix(self, mat: List[List[int]]) -> List[List[int]]:
        m = len(mat)
        n = len(mat[0])

        distance = [[-1 for _ in range(n)] for _ in range(m)]

        queue = deque()

        for i in range(m):
            for j in range(n):
                if mat[i][j] == 0:
                    distance[i][j] = 0
                    queue.append((i,j))

        directions =[(-1,0),(1,0),(0,1),(0,-1)]
        
        while len(queue) != 0 :
            r,c = queue.popleft()
            
            for dr,dc in directions:
                nr , nc = r+dr,c+dc

                if (0 <= nr < m and 0 <= nc < n and distance[nr][nc] == -1):
                    distance[nr][nc] = distance[r][c] + 1                 
                    queue.append((nr,nc))

        return distance