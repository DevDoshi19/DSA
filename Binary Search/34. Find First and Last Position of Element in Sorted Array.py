from typing import List

# brute force approach 0(n) time complexity and 0(1) space complexity
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        # low,high = 0,n-1
        lb,hb = -1,-1
        for i in range(0,n) :
            if nums[i] == target :
                if lb == -1 :
                    lb = i
                hb = i
        
        return [lb,hb]

# binary search approach 0(logn) time complexity and 0(1) space complexity
class Solution2:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        low, high = 0, n - 1
        lb = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] >= target:
                if nums[mid] == target:
                    lb = mid
                high = mid - 1
            else:
                low = mid + 1

        if lb == -1:
            return [-1,-1]

        low, high = 0, n - 1
        hb = -1

        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= target:
                if nums[mid] == target:
                    hb = mid
                low = mid + 1
            else:
                high = mid - 1

        return [lb, hb]