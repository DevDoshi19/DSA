class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        maxi = float("-inf")
        mini = float("+inf")
        global_min = float("+inf")
        global_max = float("-inf")
        
        for num in nums :
            mini = min(mini+num ,num)
            maxi = max(maxi+num,num)

            global_max = max(global_max, maxi)
            global_min = min(global_min, mini)

        return max(global_max, abs(global_min))

"""
# prefix sum apporach 

class Solution:
    def maxAbsoluteSum(self, nums: list[int]) -> int:
        current = 0
        min_prefix = 0
        max_prefix = 0
        answer = 0

        for num in nums:
            current += num

            answer = max(
                answer,
                current - min_prefix,
                max_prefix - current
            )

            min_prefix = min(min_prefix, current)
            max_prefix = max(max_prefix, current)

        return answer
"""