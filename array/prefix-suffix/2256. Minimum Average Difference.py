"""
You are given a 0-indexed integer array nums of length n.

The average difference of the index i is the absolute difference between the average of the first i + 1 elements of nums and the average of the last n - i - 1 elements. Both averages should be rounded down to the nearest integer.

Return the index with the minimum average difference. If there are multiple such indices, return the smallest one.

Note:

The absolute difference of two numbers is the absolute value of their difference.
The average of n elements is the sum of the n elements divided (integer division) by n.
The average of 0 elements is considered to be 0.
 

Example 1:

Input: nums = [2,5,3,9,5,3]
Output: 3
Explanation:
- The average difference of index 0 is: |2 / 1 - (5 + 3 + 9 + 5 + 3) / 5| = |2 / 1 - 25 / 5| = |2 - 5| = 3.
- The average difference of index 1 is: |(2 + 5) / 2 - (3 + 9 + 5 + 3) / 4| = |7 / 2 - 20 / 4| = |3 - 5| = 2.
- The average difference of index 2 is: |(2 + 5 + 3) / 3 - (9 + 5 + 3) / 3| = |10 / 3 - 17 / 3| = |3 - 5| = 2.
- The average difference of index 3 is: |(2 + 5 + 3 + 9) / 4 - (5 + 3) / 2| = |19 / 4 - 8 / 2| = |4 - 4| = 0.
- The average difference of index 4 is: |(2 + 5 + 3 + 9 + 5) / 5 - 3 / 1| = |24 / 5 - 3 / 1| = |4 - 3| = 1.
- The average difference of index 5 is: |(2 + 5 + 3 + 9 + 5 + 3) / 6 - 0| = |27 / 6 - 0| = |4 - 0| = 4.
The average difference of index 3 is the minimum average difference so return 3.
Example 2:

Input: nums = [0]
Output: 0
Explanation:
The only index is 0 so return 0.
The average difference of index 0 is: |0 / 1 - 0| = |0 - 0| = 0.
"""

class Solution:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        n = len(nums)
        if n <= 1 :
            return 0 
        prefix = [0] * (n+1) 
        suffix = [0] * (n+1) 
        for i in range(1,n+1):
            prefix[i] = prefix[i-1]+nums[i-1]
            
        for i in range(n-1,-1,-1):
            suffix[i] = suffix[i+1] + nums[i]
            
        index = None
        diff = float("inf")

        for i in range(1,n+1):
            left_div = prefix[i]//i
            if i == n :
                right_div = 0 
            else:
                right_div = suffix[i]//(n-i)
            abs_diff = abs(left_div - right_div)
            if abs_diff < diff :
                index = i - 1
                diff = abs_diff

        return index

"""
# Complexity
- Time: O(n) — building both arrays and scanning all positions.
- Auxiliary space: O(n) — the prefix and suffix arrays.
"""

# Approach 2: Using only one pass and constant space
class Solution2:
    def minimumAverageDifference(self, nums: list[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        
        left_sum = 0
        min_diff = float("inf")
        best_index = 0
        
        for i, num in enumerate(nums):
            left_sum += num
            
            # Calculate the left average
            left_avg = left_sum // (i + 1)
            
            # Calculate the right average (handle the last element carefully)
            if i == n - 1:
                right_avg = 0
            else:
                right_sum = total_sum - left_sum
                right_avg = right_sum // (n - 1 - i)
            
            # Find the absolute difference
            abs_diff = abs(left_avg - right_avg)
            
            # Track the minimum difference and its smallest index
            if abs_diff < min_diff:
                min_diff = abs_diff
                best_index = i
                
        return best_index

# Complexity
# - Time: O(n) — single pass through the array.
# - Auxiliary space: O(1) — only a few variables are used.