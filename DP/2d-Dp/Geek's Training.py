class Solution:
    def maximumPoints(self, mat):
        # code here
        day = len(mat)
        task = len(mat[0])
        
        prev = [-1] * (task+1)
        for i in range(task):
            maxi = 0
            for j in range(task):
                if i != j :
                    maxi = max(maxi,mat[0][j])
                    
            prev[i] = maxi
            
        for days in range(1,day):
            curr = [0] * (task+1)
            for last in range(0,task+1):
                maxi = 0
                for i in range(0,task):
                    if i != last : 
                        maxi = max(maxi,mat[days][i] + prev[i])
                        
                curr[last] = maxi
                
            prev = curr
            
        return prev[task]
    
# solution 2 : using recursion + memoization

class Solution2:
    def maximumPoints(self, mat):
        n = len(mat)
        m = len(mat[0])
        # dp size should be n rows and m + 1 columns (last ranges from 0 to m)
        dp = [[-1] * (m + 1) for _ in range(n)]
        
        def func(day, last, dp):
            if day == 0:
                maxi = 0
                for i in range(m):
                    if i != last:
                        maxi = max(maxi, mat[day][i])
                return maxi
                
            if dp[day][last] != -1:
                return dp[day][last]
                
            maxi = 0
            for i in range(m):
                if i != last:
                    maxi = max(maxi, mat[day][i] + func(day - 1, i, dp))
                    
            dp[day][last] = maxi
            return dp[day][last]
            
        # Start from the last day with 'm' as the initial last state
        return func(n - 1, m, dp)
