from typing import List,Tuple

# Approach 1 : Using bit manipulation to generate all subsets and using a set to avoid duplicates. The time complexity of this approach is O(n * 2^n) where n is the number of elements in the input array. This is because we are generating 2^n subsets and for each subset, we are iterating through n elements to check if they are included in the subset or not.

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        n = len(nums)
        total_subset = 1<<n 
        result = []
        seen = set()
        for num in range(total_subset):
            lst = []
            for i in range(n):
                if num & (1<<i) != 0 :
                    lst.append(nums[i])

            key = tuple(lst)
            if key not in seen :
                seen.add(key)
                result.append(list(key))

        return result
    
    
