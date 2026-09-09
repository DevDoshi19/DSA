from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        n = len(arr)
        if n == 3 :
            return 1
        
        low,high=0,n-1

        while low < high:
            mid = (low+high) // 2
            
            if arr[mid] > arr[mid+1] :
                high = mid
            else :
                low = mid+1
            
        return low
