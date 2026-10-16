from collections import Counter

# time complexity: O(n)
# space complexity: O(n)
class Solution:
    def majorityElement(self, nums: list[int]) -> list[int]:

        freq = Counter(nums)
        n = len(nums)
        length = n // 3
        ans = []
        for key,value in freq.items():
            if value > length :
                ans.append(key)

        return ans