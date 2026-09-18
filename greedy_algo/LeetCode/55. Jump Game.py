from typing import List
class Solution:
    """
    Working : 
    1. We can use a greedy approach to solve this problem.
    2. We can keep track of the maximum index we can reach at each step.
    3. If at any point, the current index is greater than the maximum index we can reach, we return False.
    4. If we reach the end of the array, we return True.
    """
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
    
s = Solution()
print(s.canJump([2,3,1,1,4])) # True
# here the maximum index we can reach is 4, which is the last index of the array.
print(s.canJump([3,2,1,0,4])) # False
# here the maximum index we can reach is 3, which is less than the last index of the array.
