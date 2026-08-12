"""
# Maximum Size Subarray Sum Equals k

Given an array `nums` and integer `k`, find the length of the **longest** subarray that sums to exactly `k`.

```
nums = [1, -1, 5, -2, 3], k = 3
Output: 4   // [1, -1, 5, -2] sums to 3, length 4
```

You have everything you need from problems 1 and 3:
- From **Problem 1**: the lookup value is `prefix - k` (the "need").
- From **Problem 3**: the hashmap stores **first index only**, not counts — because we want max length.

Answer these two quick questions first:
1. Each iteration, what value do you look up in the hashmap?
2. When that value is found, what do you compute — and do you overwrite the hashmap entry for `prefix` if it already exists?

Then write the code.
"""
from typing import List
class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:
        max_len = 0
        prefix_sum = 0
        prefix_sum_map = {0: -1}
        for i in range(len(nums)) :
            prefix_sum += nums[i]
            need = prefix_sum - k 
            if need in prefix_sum_map :
                max_len = max(max_len,i-prefix_sum_map[need])
            if prefix_sum not in prefix_sum_map:
                prefix_sum_map[prefix_sum] = i
        
        return max_len

nums = [1, -1, 5, -2, 3]
k = 3
s = Solution()
print(s.maxSubArrayLen(nums,k)) # 4