from typing import List
class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        m = len(grid)
        n = len(grid[0])
        dp = [[-1 for _ in range(n)] for _ in range(m)]

        def backtrack(row,col,dp):
            if row >= m or col >= n :
                return float("inf")

            if row == m - 1 and col == n - 1:
                return grid[row][col]

            if dp[row][col] != -1 :
                return dp[row][col]

            right = backtrack(row,col+1,dp)
            down = backtrack(row+1,col,dp)

            dp[row][col] = grid[row][col] + min(right,down)
            return dp[row][col]

        return backtrack(0,0,dp)
