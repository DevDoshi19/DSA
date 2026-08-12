from typing import List


class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix = 0
        prefix_sum = {0:1}
        count = 0

        for num in nums :
            prefix += num
            remainder = prefix % k
            if remainder in prefix_sum :
                count += prefix_sum[remainder]
            
            prefix_sum[remainder] = prefix_sum.get(remainder,0)+1
            

        return count

