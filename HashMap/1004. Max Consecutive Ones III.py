from typing import List
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = 0
        zero_count = 0
        max_total = 0

        for right in range(len(nums)):
            if nums[right] == 0 :
                zero_count +=1 

            while zero_count > k:
                if nums[left] == 0 :
                    zero_count -=1
                left += 1    
        
            max_total = max(max_total,right-left+1)

        return max_total 


