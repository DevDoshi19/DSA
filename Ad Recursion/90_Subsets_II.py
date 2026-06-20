from typing import List

# approch 2 : Using backtracking to generate all subsets and using a set to avoid duplicates. The time complexity of this approach is O(2^n) where n is the number of elements in the input array. This is because we are generating 2^n subsets, but it does not require iterating through n elements for each subset. The space complexity is O(n) for the recursion stack and O(2^n) for storing the subsets in the result list.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        result = []
        seen = set()
        def solve(index,subset):
            if index >= n :
                sub = tuple(subset.copy())
                if sub not in seen :
                    seen.add(sub)
                    result.append(subset.copy())
                return
            subset.append(nums[index])
            solve(index+1,subset)
            subset.pop()
            solve(index+1,subset)

        solve(0,[])

        return result
    
# Time complexity : O(2^n) where n is the number of elements in the input array. This is because we are generating 2^n subsets, but it does not require iterating through n elements for each subset. The space complexity is O(n) for the recursion stack and O(2^n) for storing the subsets in the result list.