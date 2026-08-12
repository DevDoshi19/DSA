from typing import List

class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        prefix = 0
        hashmap = {0: -1}

        for i in range(len(nums)):
            prefix += nums[i]

            if k == 0:
                key = prefix
            else:
                key = prefix % k

            if key in hashmap:
                if i - hashmap[key] >= 2:
                    return True
            else:
                hashmap[key] = i

        return False