from typing import List

# T.C. O(9^n) s.c. = O(n) for recursion
# for dp t.c. = O(n*m*m*9) s.c. = O(n*m*m)

class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        r = len(grid) 
        c = len(grid[0])
        
        def backtrack(i,j1,j2,dp):
            if j1 < 0 or j1 > c-1 or j2<0 or j2>c-1:
                return float("-inf")

            if i == r-1 :
                if j1 == j2 :
                    return grid[i][j1]
                else :
                    return grid[i][j1]+grid[i][j2]

            if dp[i][j1][j2] != float("-inf"):
                return dp[i][j1][j2]
            
            maxi = 0
            for new_j1 in range(-1,2):
                for new_j2 in range(-1,2):
                    if j1 == j2 :
                        ans = grid[i][j1] + backtrack(i+1,j1+new_j1,j2+new_j2,dp)
                    else :
                        ans = grid[i][j1] + grid[i][j2] + backtrack(i+1,j1+new_j1,j2+new_j2,dp)

                    maxi = max(maxi,ans)
                    dp[i][j1][j2] = maxi

            return maxi

        dp =[[[float("-inf") for _ in range(c)] for _ in range(c)] for _ in range(r)]
        return backtrack(0,0,c-1,dp)

# t.c. = O()    
class Solution2:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        r = len(grid) 
        c = len(grid[0])
        # r x c x c
        dp =[[[float("-inf") for _ in range(c)] for _ in range(c)] for _ in range(r)]
        for j1 in range(c):
            for j2 in range(c):
                if j1 == j2 :
                    dp[r-1][j1][j2] = grid[r-1][j1]
                else :
                    dp[r-1][j1][j2] = grid[r-1][j1]+grid[r-1][j2]

        for i in range(r-2,-1,-1):
            for j1 in range(c):
                for j2 in range(c):
                    maxi = 0 
                    for new_j1 in range(-1,2):
                        for new_j2 in range(-1,2):
                            if new_j1+j1 <0 or new_j1+j1 >= c or new_j2+j2<0 or new_j2+j2 >= c :
                                ans = float("-inf")
                            elif j1 == j2 :
                                ans = grid[i][j1] + dp[i+1][j1+new_j1][j2+new_j2]
                            else :
                                ans = grid[i][j1] + grid[i][j2] + dp[i+1][j1+new_j1][j2+new_j2]

                            maxi = max(maxi,ans)
                    dp[i][j1][j2]= maxi
                    
        return dp[0][0][c-1]