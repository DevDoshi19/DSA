class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1 

        def path(row,col):
            if row >= m or col >= n :
                return 0

            if row == m-1 and col == n-1 :
                return 1 

            total1 = path(row,col+1)
            total2 = path(row+1,col)

            return total1+total2

        return path(0,0)
    
# solution 2 which is recursive with memoization
class Solution2:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1 

        def path(row,col,dp):
            if row >= m or col >= n :
                return 0

            if row == m-1 and col == n-1 :
                return 1 

            if dp[row][col] != -1 :
                return dp[row][col]

            total1 = path(row,col+1,dp)
            total2 = path(row+1,col,dp)

            dp[row][col] = total1+total2

            return dp[row][col]

        dp = [[-1]*n for _ in range(m)]
        return path(0,0,dp)
    
# approch 3 which is iterative with tabulation
class Solution3:
    def uniquePaths(self, m: int, n: int) -> int:
        if m == 1 or n == 1:
            return 1 

        dp = [[1]*n for _ in range(m)]
        
        for i in range(1,m):
            for j in range(1,n) :
                dp[i][j] = dp[i-1][j]+dp[i][j-1]  
        
        return dp[m-1][n-1]