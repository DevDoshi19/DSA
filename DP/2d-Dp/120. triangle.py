from typing import List
class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        m = len(triangle)
        def backtrack(row,col,dp):
            if row >= m :
                return 0
            if (row,col) in dp:
                return dp[(row,col)]

            down = backtrack(row+1,col,dp)
            dig = backtrack(row+1,col+1,dp)

            dp[(row,col)] = triangle[row][col]+min(down,dig)

            return dp[(row,col)]

        dp = {}

        return backtrack(0,0,dp)

# tabluation with space optimization
class Solution2:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        n = len(triangle)

        prev = triangle[-1][:]

        for i in range(n - 2, -1, -1):
            curr = [0] * (i + 1)

            for j in range(i + 1):
                down = triangle[i][j] + prev[j]
                diagonal = triangle[i][j] + prev[j + 1]

                curr[j] = min(down, diagonal)

            prev = curr

        return prev[0]