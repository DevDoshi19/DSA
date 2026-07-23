from typing import List
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        n = len(nums)
        left,right =0,n-1
        mid = 0

        while left <= right :
            mid = (left+right) //2

            if nums[mid] == target :
                return mid
            
            if nums[left] <= nums[mid] :
                if nums[left] <= target < nums[mid] :
                    right = mid -1
                else :
                    left = mid +1 
            else :
                if nums[mid] < target <= nums[right] :
                    left= mid+1
                else :
                    right = mid-1

        return -1