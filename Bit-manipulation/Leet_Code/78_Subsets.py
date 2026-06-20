from typing import List
class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 0 :
            return [[]]
        
        n = len(nums)
        total_subset = 1 << n
        result = []

        for num in range(0,total_subset):
            lst = []
            for i in range(0,n):
                if num & (1 << i) != 0 :
                    lst.append(nums[i])

            result.append(lst)

        return result 
    
    
# Time complexity : O(n * 2^n) where n is the number of elements in the input array. This is because we are generating 2^n subsets and for each subset, we are iterating through n elements to check if they are included in the subset or not.

# one more approach is to use backtracking to generate all subsets. This approach has a time complexity of O(2^n) as we are generating 2^n subsets, but it does not require iterating through n elements for each subset.