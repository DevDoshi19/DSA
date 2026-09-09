# https://www.geeksforgeeks.org/problems/number-of-occurrence2259/1

class Solution:
    def countFreq(self, arr, target):
        # code here
        n = len(arr)
        low,high = 0,n-1
        lb ,hb=-1,n
        
        while low <= high:
            mid = (low+high) //2 
            if arr[mid] >= target :
                lb = mid 
                high = mid -1 
            else :
                low = mid +1
                
        if lb == -1 :
            return 0
                
        low,high = 0,n-1  
        while low <= high :
            mid = (low+high) // 2
            if arr[mid] <= target :
                low = mid + 1
            else :
                hb = mid
                high = mid -1
                
        return hb-lb