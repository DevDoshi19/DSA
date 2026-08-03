from typing import List
class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n is None :
            return 0
        if n == 1:
            return nums[0]

        def backtrack(start, end):
            dp = [-1] * n
            
            dp[start] = nums[start]
            dp[start + 1] = max(nums[start], nums[start + 1])
            
            for i in range(start + 2, end + 1): 
                pick = nums[i] + dp[i - 2]
                not_pick = dp[i - 1]
                dp[i] = max(pick, not_pick)
                
            return dp[end]

        i1 = backtrack(0,n-2)
        i2 = backtrack(1,n-1) 

        return max(i1,i2)  