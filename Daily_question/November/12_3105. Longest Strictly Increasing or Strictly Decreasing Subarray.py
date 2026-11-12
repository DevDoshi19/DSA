from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1:
            return n
        max_long = 0
        count_inc = 1
        count_dec = 1
        for i in range(1,n):
            if nums[i] > nums[i-1]:
                count_inc += 1
                count_dec = 1
            elif nums[i] < nums[i-1]:
                count_dec += 1
                count_inc = 1
            else:
                count_inc = 1
                count_dec = 1

            max_long = max(max_long,count_inc,count_dec)

        return max_long