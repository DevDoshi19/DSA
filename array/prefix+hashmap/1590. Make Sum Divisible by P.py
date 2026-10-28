class Solution:
    def minSubarray(self, nums: list[int], p: int) -> int:
        total = sum(nums)
        target = total % p

        if target == 0:
            return 0

        prefix_map = {0: -1}
        prefix = 0
        n = len(nums)
        answer = n

        for i,num in enumerate(nums):
            prefix = ( prefix + num ) % p 
            needed = (prefix - target) % p 

            if needed in prefix_map :
                answer = min(answer, i - prefix_map[needed] )

            prefix_map[prefix] = i 
        
        return answer if answer != n else -1 