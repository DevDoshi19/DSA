"""
41. First Missing Positive

Given an unsorted integer array nums. Return the smallest positive integer that is not present in nums.
You must implement an algorithm that runs in O(n) time and uses O(1) auxiliary space.

Example 1:
Input: nums = [1,2,0]
Output: 3
Explanation: The numbers in the range [1,2] are all in the array.

Example 2:
Input: nums = [3,4,-1,1]
Output: 2
Explanation: 1 is in the array but 2 is missing.
 
"""

class Solution:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)

        for num in range(1,n+2):
            if num not in nums:
                return num
            
        """
        ~ For an array of length \(n\), the smallest missing positive must be in the range \(1\) through \(n+1\). If all numbers from \(1\) through \(n\) exist, then \(n+1\) must be missing.
        - Time: O(n) average.
        - Extra space: O(n).
        """

# Cyclic Sort or Index Placement
class solution2:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        for i in range(n):
            while 1 <= nums[i] <= n and nums[nums[i]-1] != nums[i]:
                nums[nums[i]-1], nums[i] = nums[i], nums[nums[i]-1]

        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
        return n + 1

        """
        ~ For an array of length \(n\), the smallest missing positive must be in the range \(1\) through \(n+1\). If all numbers from \(1\) through \(n\) exist, then \(n+1\) must be missing.
        - Time: O(n).
        - Extra space: O(1).
        """

class Solution3:
    def firstMissingPositive(self, nums: list[int]) -> int:
        n = len(nums)
        new_nums = set(nums)
        for num in range(1,n+2):
            if num not in new_nums:
                return num