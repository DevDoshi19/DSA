from typing import List

class Solution:

    # check if the array is rotated or not and then apply binary search
    """
    step 1 : check if the low, mid and high are equal then we can not identify the sorted part of the array so we will reduce the search space by reducing the high and increasing the low 
    step 2 : identify the sorted part of the array
    step 3 : check if the target is in the sorted part or not
    step 4 : if the target is in the sorted part then apply binary search on that part
    step 5 : if the target is not in the sorted part then apply binary search on the other part
    step 6 : if the target is not found then return -1
    """

    def search(self, nums: List[int], target: int) -> bool:
        n = len(nums)
        low, high = 0 ,n-1
        while low <= high :
            mid = (low + high) // 2
            if nums[mid] == target :
                return True 
            if nums[mid] == nums[low] == nums[high] :
                high -=1
                low +=1
                continue
            if nums[low] <= nums[mid] :
                if nums[low] <= target < nums[mid]:
                    high = mid - 1
                else :
                    low = mid + 1
            else :
                if nums[mid] < target <= nums[high]:
                    low = mid + 1
                else :
                    high = mid - 1

        return False