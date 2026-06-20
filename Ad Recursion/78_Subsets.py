from typing import List

# Approach 2 : using backtracking , T.c. = O(2^n) where n is the number of elements in the input array. This is because we are generating 2^n subsets, but it does not require iterating through n elements for each subset. The space complexity is O(n) for the recursion stack and O(2^n) for storing the subsets in the result list.

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        result = []
        
        def solve(index,subset):
            if index >= len(nums):
                result.append(subset.copy())
                return 
            
            subset.append(nums[index])
            solve(index+1,subset)
            subset.pop()
            solve(index+1,subset)

        solve(0,[])
        return result 