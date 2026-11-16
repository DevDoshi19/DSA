from typing import List


class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # mini_sum = float("inf")
        # curr_sum = 0
        # for i in range(l):
        #     curr_sum += nums[i]

        # if curr_sum > 0 :
        #     mini_sum = curr_sum
        
        # i = 0
        # j = r-1
        # n = len(nums)
        # while j < n :
        #     curr_sum += nums[j]
        #     if curr_sum > 0 :
        #         mini_sum = min(mini_sum,curr_sum)
            
        #     while j-i+1 > l :
        #         curr_sum -= nums[i]
        #         if curr_sum > 0 :
        #             mini_sum = min(mini_sum,curr_sum)
        #         i+=1
            
        #     j+=1

        # return mini_sum if mini_sum != float("inf") else -1 

        n = len(nums)
        mini_sum = float("inf")
        
        for size in range(l, r + 1):
            curr_sum = sum(nums[:size])
            if curr_sum > 0:
                mini_sum = min(mini_sum, curr_sum)
                
            for j in range(size, n):
                curr_sum += nums[j] - nums[j - size]
                if curr_sum > 0:
                    mini_sum = min(mini_sum, curr_sum)
                    
        return mini_sum if mini_sum != float("inf") else -1

class Solution2:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # new approach - brute force  
        mini = float("inf")
        n = len(nums)
        for i in range(n-l+1):
            total = 0
            for j in range(i+l-1,n):
                if l<= j-i+1 <= r :
                    total = sum(nums[i:j+1])
                    if total > 0:
                        mini = min(mini,total)
            
        return mini if mini != float("inf") else -1