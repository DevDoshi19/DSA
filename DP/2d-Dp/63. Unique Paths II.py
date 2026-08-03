from typing import List
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        def backtrack(row,col,dp):
            if row >= m or col >= n :
                return 0
            if obstacleGrid[row][col] == 1 :
                return 0
            if row == m-1 and col == n-1 :
                return 1
            if dp[row][col] != -1 :
                return dp[row][col]

            right = backtrack(row,col+1,dp)
            down = backtrack(row+1,col,dp)

            dp[row][col] = right+down
            return dp[row][col]

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        
        return backtrack(0,0,dp)
    


class Solution2:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [0 for _ in range(n)]
        if obstacleGrid[0][0] == 1 :
            return 0

        dp[0] = 1

        for i in range(0,m):
            for j in range(0,n):

                if obstacleGrid[i][j] == 1 :
                    dp[j]=0
                else :
                    if j > 0:
                        dp[j] += dp[j-1]

        return dp[n-1]
    
class Solution3:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])

        dp = [[-1 for _ in range(n)] for _ in range(m)]
        if obstacleGrid[0][0] == 1 :
            return 0
        dp[0][0] = 1

        for i in range(0,m):
            for j in range(0,n):
                if i == 0 and j == 0 :
                    continue

                if obstacleGrid[i][j] == 1 :
                    dp[i][j]=0
                    continue

                if i == 0 :
                    up = 0
                else :
                    up = dp[i-1][j]
                if j == 0 :
                    left = 0
                else :
                    left= dp[i][j-1]

                dp[i][j] = up +left

        return dp[m-1][n-1]