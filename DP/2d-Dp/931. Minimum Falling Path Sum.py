from typing import List
class Solution:

    # TLE error 
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        def backtrack(row,col,dp):
            if col < 0 or col >= n:
                return float("inf")

            if row == m - 1:
                return matrix[row][col] 
            
            if dp[row][col] != -1 :
                return dp[row][col]

            leftdia = backtrack(row+1,col-1,dp)
            down = backtrack(row+1,col,dp)
            rightdia = backtrack(row+1,col+1,dp)

            dp[row][col] = matrix[row][col] + min(leftdia,down,rightdia)
            return dp[row][col]

        ans = float("inf")
        dp = [[-1 for _ in range(n)] for _ in range(m)]
        for col in range(0,n):
            ans = min(ans,backtrack(0,col,dp))

        return ans
    
# tabluation approach 
class Solution2:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        dp = [[0] * n for _ in range(m)]

        for j in range(n):
            dp[m-1][j] = matrix[m-1][j]

        for i in range(m-2,-1,-1):
            for j in range(n):
                down = dp[i+1][j] 
                leftdig = dp[i+1][j-1] if j > 0 else float("inf")
                rightdig = dp[i+1][j+1] if j < n-1 else float("inf")

                dp[i][j] = matrix[i][j] + min(down,leftdig,rightdig)

        return min(dp[0])
    

# tabulation approach with space optimization
class Solution3:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        m = len(matrix)
        n = len(matrix[0])
        prev = [0] * n 

        for j in range(n):
            prev[j] = matrix[m-1][j]

        for i in range(m-2,-1,-1):
            curr = [0] * n 
            for j in range(n):
                down = prev[j] 
                leftdig = prev[j-1] if j > 0 else float("inf")
                rightdig = prev[j+1] if j < n-1 else float("inf")

                curr[j] = matrix[i][j] + min(down,leftdig,rightdig)

            prev = curr.copy()

        return min(prev)