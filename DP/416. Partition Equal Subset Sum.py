from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        n = len(nums)

        total = sum(nums)
        if total % 2 != 0 :
            return False 

        target = total //2 

        def backtrack(index,current_target):
            if current_target == target:
                return True
            if index >= n or current_target > target:
                return False

            pick = backtrack(index+1,current_target+nums[index])
            if pick :
                return True

            not_pick = backtrack(index+1,current_target)
            if not_pick:
                return True

            return pick or not_pick
            
        return backtrack(0,0)
    
