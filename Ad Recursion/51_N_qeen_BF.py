
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1 :
            return [["Q"]]
        
        ans:list = []
        board = ["."*n for _ in range(n)]
        
        def isSafe(row,col,board,n):
            duprow = row
            dupcol = col

            while row >= 0 and col >= 0 :
                if board[row][col] == "Q":
                    return False
                row -=1
                col -=1

            row = duprow
            col = dupcol

            while col >= 0:
                if board[row][col] == "Q":
                    return False
                col-=1
        
            col = dupcol
            while row < n and col >= 0 :
                if board[row][col] == "Q":
                    return False
                col-=1
                row+=1

            return True

        def backtrack(col,board,ans,n):
            if col == n :
                ans.append(list(board))
                return 

            for row in range(n) :
                if isSafe(row,col,board,n):
                    board[row] = board[row][:col] +"Q"+ board[row][col+1:]
                    backtrack(col+1,board,ans,n)
                    board[row] = board[row][:col] +"."+ board[row][col+1:]
        
        backtrack(0,board,ans,n)

        return ans

             