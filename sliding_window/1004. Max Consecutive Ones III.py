from typing import List 
class Best:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = 0
        zero_count = 0
        max_total = 0

        for right in range(0,len(nums)):
            if nums[right] == 0 :
                zero_count += 1
            
            if zero_count > k :
                if nums[left] == 0 :
                    zero_count -=1 
                left += 1

            if zero_count <= k :
                max_total = max(max_total,right-left+1)

        return max_total 

# Because of IF the t.c. become O(n) In one pass and s.c. O(1)  .... 
# we are not chaining the max window size , once we find it , so we are doing just if else opreation , whether the zero is more or < k ? if more then just left+=1 , and if less then we are just calculating the max window size and return it at the end of the loop.

class BetterNotBest:
    def longestOnes(self, nums: List[int], k: int) -> int:
        
        left = 0
        zero_count = 0
        max_total = 0

        for right in range(0,len(nums)):
            if nums[right] == 0 :
                zero_count += 1
            
            while zero_count > k :
                if nums[left] == 0 :
                    zero_count -=1 
                left += 1

            
            max_total = max(max_total,right-left+1)

        return max_total 
    
# Here we also get an same output but we are using while loop instead of if , so we are doing more operation than the first one , because we are checking the condition of zero count > k in while loop and in if we are just checking once and then we are doing the operation. So the first one is better than this one.
# t.c. O(n) + O(n) = O(2n) which is similar to O(n) and s.c. O(1)


"""
    Brute force is trying to find all the substring with i and j (2 loops)
"""