from typing import List
# https://leetcode.com/problems/split-array-largest-sum/solutions/6695631/understanding-the-optimal-way-problem-pa-v8u0

class Solution:
    def canSplit(self,nums,capacity,k):
        parts = 1
        current_capacity = 0 
        for num in nums:
            if current_capacity+num > capacity :
                current_capacity = num
                parts += 1
            else :
                current_capacity += num

        return parts <= k

    def splitArray(self, nums: List[int], k: int) -> int:
        low = max(nums)
        high = sum(nums)

        while low < high :
            capacity = (low+high) // 2
            if self.canSplit(nums,capacity,k):
                high = capacity
            else:
                low = capacity + 1
        
        return low
