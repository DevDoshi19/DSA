# from functools import lru_cache
class Solution:
    def minCost(self, height):
        # code here
        n = len(height)
        
        if n <= 0:
            return -1
        if n == 1:
            return 0
            
        dp = [float("inf")] * n
        dp[0] = 0
        dp[1] = abs(height[1] - height[0])
        
        for i in range(2,n):
            func1 =dp[i-1] + abs(height[i]-height[i-1])
            func2 =dp[i-2] + abs(height[i]-height[i-2])
            dp[i] = min(func1,func2)
            
        return dp[n-1]
        
# using tabulation method + space optimization 
class Solution2:
    def minCost(self, height):
        # code here
        n = len(height)
        
        if n <= 0:
            return -1
        if n == 1:
            return 0
            
        
        prev2 = 0
        prev1 = abs(height[1] - height[0])
        
        for i in range(2,n):
            func1 = prev1 + abs(height[i] - height[i-1])
            func2 = prev2 + abs(height[i]-height[i-2])
            prev2 = prev1
            prev1 = min(func1,func2)
            
        return prev1
        
# using recursion + memoization
class Solution3:
    def minCost(self, height):
        # code here 
        n = len(height)

        def func(i,dp):
            if i == 0:
                return 0
            if i == 1:
                return abs(height[1] - height[0])
            if dp[i] != -1:
                return dp[i]
            
            func1 = func(i-1,dp) + abs(height[i]-height[i-1])
            func2 = func(i-2,dp) + abs(height[i]-height[i-2])
            dp[i] = min(func1,func2)
            return dp[i]
        
        dp = [-1] * n
        return func(n-1,dp)