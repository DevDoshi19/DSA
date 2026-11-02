"""
Given an integer array nums of size n, return the minimum number of moves required to make all array elements equal.
In one move, you can increment or decrement an element of the array by 1.
Test cases are designed so that the answer will fit in a 32-bit integer.

Example 1:

Input: nums = [1,2,3]
Output: 2
Explanation:
Only two moves are needed (remember each move increments or decrements one element):
[1,2,3]  =>  [2,2,3]  =>  [2,2,2]
"""

class Solution:
    def minMoves2(self, nums: list[int]) -> int:
        nums.sort() 
        n = len(nums)    
        mid = n // 2  # 1 
        val = nums[mid]
        total = 0 
        for num in nums : # n 
            total += abs(num-val)

        return total # n + nlogn = nlogn
    
"""
The simple thing is to find the middle , cause we know that to get the least number of change we need to take a number which is not maximum neither minimum , 
but the middle number always give us the least number of change to make all numbers equal to it.

"""