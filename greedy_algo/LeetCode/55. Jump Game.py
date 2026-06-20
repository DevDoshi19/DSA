from typing import List
class Solution:
    def canJump(self, nums: List[int]) -> bool:
        if len(nums) <= 1:
            return True
        if nums[0] == 0 and len(nums) > 1:
            return False

        n = len(nums)
        max_index = 0 

        for i in range(n):
            if i > max_index :
                return False

            max_index = max(max_index,i+nums[i])

        return True
