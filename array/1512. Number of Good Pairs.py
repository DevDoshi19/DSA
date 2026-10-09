from typing import Counter


class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        # i = 0 
        n = len(nums)
        if n <= 1:
            return 0 
        
        # count = 0
        # while i < n-1 :
        #     j = i + 1
        #     while j < n :
        #         if nums[i] == nums[j] :
        #             count += 1
        #         j+= 1
        #     i+=1
        # return count

        count = 0
        freq = Counter(nums)
        for key,value in freq.items():
            if value > 1 :
                count += ((value * (value-1))//2)
            
        return count