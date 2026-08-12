from typing import List

class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i] == 0:
                nums[i] = -1
        
        prefix = 0
        prefix_sum = {0:-1}
        max_len = 0

        for i in range(len(nums)) :
            prefix += nums[i]
            if prefix in prefix_sum:
                max_len = max(max_len,i-prefix_sum[prefix])
            else:
                prefix_sum[prefix] = i 
    
        return max_len