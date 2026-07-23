class Solution:
    # simple recursion + memoization approch 
    # t.c. O(n) s.c. O(n) + O(n) for recursion stack
    def climbStairs(self, n: int) -> int:
        def func(num,dp):
            if num <= 2 :
                return num
            if dp[num] != -1 :
                return dp[num]

            dp[num] = func(num-1,dp) + func(num-2,dp)
            return dp[num]

        dp = [-1] * (n+1)
        return func(n,dp) 

# approch 2 if for the tabulation method we can use the same logic as above but we will use a for loop to fill the dp array instead of recursion
class Solution2:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n+1)
        dp[0] = 0
        dp[1] = 1
        if n >= 2:
            dp[2] = 2
        for i in range(3, n+1):
            dp[i] = dp[i-1] + dp[i-2]
        return dp[n]
           
class Solution3:
    def climbStairs(self, n: int) -> int:
        if n <= 2:
            return n

        prev2 = 1
        prev1 = 2

        for i in range(2,n):
            current = prev2 + prev1
            prev2 = prev1
            prev1 = current

        return current
        
