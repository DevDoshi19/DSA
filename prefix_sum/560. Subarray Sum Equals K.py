from typing import List
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:

        prefix_sum = {0:1}
        current_sum = 0
        needed = 0 
        count = 0

        for num in nums :
            current_sum += num
            needed = current_sum - k
            if needed in prefix_sum :
                count += prefix_sum[needed]

            prefix_sum[current_sum] = prefix_sum.get(current_sum,0) + 1

        return count