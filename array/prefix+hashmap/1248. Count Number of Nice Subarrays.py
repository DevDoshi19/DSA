class Solution:
    def numberOfSubarrays(self, nums: list[int], k: int) -> int:
        n = len(nums)
        count = 0
        prefix_map = {0:1}
        if n < k :
            return 0 

        prefix = 0 
        for i in range(n):
            if nums[i] % 2 == 1 :
                prefix += 1
                
            rem = prefix - k 
            if rem in prefix_map : 
                count += prefix_map[rem]
            
            prefix_map[prefix] = prefix_map.get(prefix,0)+1 
            
        return count 