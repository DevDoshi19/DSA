from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        n = len(nums)
        right = n-1

        while left <= right :
            mid = (left + right) //2 

            if nums[mid] == target:
                return mid
            elif nums[mid] > target :
                right = mid-1
            elif nums[mid] < target :
                left = mid + 1

        return -1