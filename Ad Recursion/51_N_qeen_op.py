
from typing import List

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        if n == 1 :
            return [["Q"]]
        
        ans:List[List[str]] = []
        board = ["."*n for _ in range(n)]
        hor = ["0"]* n
        negdig = ["0"]* ( 2*n -1 )
        posdig = ["0"]* ( 2*n -1 )
        
        def isSafe(horVal,negVal,posVal,board,n):
            if hor[horVal] == "1":
                return False

            if negdig[negVal] == "1":
                return False

            if posdig[posVal] == "1":
                return False

            return True

        def backtrack(col,board,ans,n):
            if col == n :
                ans.append(board[:])
                return 

            for row in range(n) :
                horVal = row 
                negVal = (col+row)
                posVal = (n-1) + (col-row)

                if isSafe(horVal,negVal,posVal,board,n):
                    
                    posdig[posVal] ,negdig[negVal],hor[horVal]= "1", "1", "1"

                    board[row] = board[row][:col] +"Q"+ board[row][col+1:]
                    
                    backtrack(col+1,board,ans,n)
                    
                    posdig[posVal] ,negdig[negVal],hor[horVal]= "0", "0", "0"
                    
                    board[row] = board[row][:col] +"."+ board[row][col+1:]
        
        backtrack(0,board,ans,n)

        return ans

s = Solution()
print(s.solveNQueens(4))