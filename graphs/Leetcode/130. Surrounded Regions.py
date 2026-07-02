from typing import List
from collections import deque

class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])

        q = deque()

        for i in range(m):
            if board[i][0] == "O" :
                q.append((i,0))
            if board[i][n-1] == "O":
                q.append((i,n-1))

        for j in range(n):
            if board[0][j] == "O" :
                q.append((0,j))
            if board[m-1][j] == "O":
                q.append((m-1,j))

        directions = [(-1,0),(1,0),(0,1),(0,-1)]

        while q :
            r,c = q.popleft()
            board[r][c] = "#"

            for i,j in directions:
                nr,nc = r+i,c+j

                if 0<=nr<m and 0<=nc<n and board[nr][nc] == "O":
                    q.append((nr,nc))
                    board[nr][nc] = "#"

                
        for i in range(m):
            for j in range(n):
                if board[i][j] == "O":
                    board[i][j] = "X"
                elif board[i][j] == "#":
                    board[i][j] = "O"
                
        return board
    
# simply use bfs :

"""
step 1 :  find all the "O" on the border and add them in queue
step 2 :  mark them as "#" and add them to the queue
step 3 :  for each element in the queue, check its neighbors and if they are "O" mark them as "#" and add them to the queue
step 4 :  after the bfs is done, all the "O" that are not marked as "#" are surrounded by "X" and can be changed to "X"

"""