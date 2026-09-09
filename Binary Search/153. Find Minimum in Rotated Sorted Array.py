from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        n = len(nums)
        low,high = 0 ,n-1
        while low < high :
            mid = (low+high) // 2 
            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid 

        return nums[low]

# not optimal
class Solution2:
    def findMin(self, nums: List[int]) -> int:
        mini = float("inf")
        n = len(nums)
        low,high = 0 ,n-1
        while low <= high :
            mid = (low+high) // 2 
            mini = min(mini,nums[mid])
            if nums[low] <= nums[mid] :
                if nums[mid] >= nums[high] :
                    low = mid + 1 
                else :
                    high = mid -1 
            else:
                if nums[mid] <= nums[high] :
                    high = mid - 1
                else :
                    low = mid + 1

        return mini 