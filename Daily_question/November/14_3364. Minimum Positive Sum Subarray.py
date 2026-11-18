from typing import List

"""
You are given an integer array nums and two integers l and r. Your task is to find the minimum sum of a subarray whose size is between l and r (inclusive) and whose sum is greater than 0.

Return the minimum sum of such a subarray. If no such subarray exists, return -1.

A subarray is a contiguous non-empty sequence of elements within an array.

 

Example 1:

Input: nums = [3, -2, 1, 4], l = 2, r = 3

Output: 1

Explanation:

The subarrays of length between l = 2 and r = 3 where the sum is greater than 0 are:

[3, -2] with a sum of 1
[1, 4] with a sum of 5
[3, -2, 1] with a sum of 2
[-2, 1, 4] with a sum of 3
Out of these, the subarray [3, -2] has a sum of 1, which is the smallest positive sum. Hence, the answer is 1.

Example 2:

Input: nums = [-2, 2, -3, 1], l = 2, r = 3

Output: -1

Explanation:

There is no subarray of length between l and r that has a sum greater than 0. So, the answer is -1.

Example 3:

Input: nums = [1, 2, 3, 4], l = 2, r = 4

Output: 3

Explanation:

The subarray [1, 2] has a length of 2 and the minimum sum greater than 0. So, the answer is 3.

 

Constraints:

1 <= nums.length <= 100
1 <= l <= r <= nums.length
-1000 <= nums[i] <= 1000
"""
class Solution:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # mini_sum = float("inf")
        # curr_sum = 0
        # for i in range(l):
        #     curr_sum += nums[i]

        # if curr_sum > 0 :
        #     mini_sum = curr_sum
        
        # i = 0
        # j = r-1
        # n = len(nums)
        # while j < n :
        #     curr_sum += nums[j]
        #     if curr_sum > 0 :
        #         mini_sum = min(mini_sum,curr_sum)
            
        #     while j-i+1 > l :
        #         curr_sum -= nums[i]
        #         if curr_sum > 0 :
        #             mini_sum = min(mini_sum,curr_sum)
        #         i+=1
            
        #     j+=1

        # return mini_sum if mini_sum != float("inf") else -1 

        n = len(nums)
        mini_sum = float("inf")
        
        for size in range(l, r + 1):
            curr_sum = sum(nums[:size])
            if curr_sum > 0:
                mini_sum = min(mini_sum, curr_sum)
                
            for j in range(size, n):
                curr_sum += nums[j] - nums[j - size]
                if curr_sum > 0:
                    mini_sum = min(mini_sum, curr_sum)
                    
        return mini_sum if mini_sum != float("inf") else -1

class Solution2:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        # new approach - brute force  
        mini = float("inf")
        n = len(nums)
        for i in range(n-l+1):
            total = 0
            for j in range(i+l-1,n):
                if l<= j-i+1 <= r :
                    total = sum(nums[i:j+1])
                    if total > 0:
                        mini = min(mini,total)
            
        return mini if mini != float("inf") else -1

class Solution3:
    def minimumSumSubarray(self, nums: List[int], l: int, r: int) -> int:
        mini = float("inf")
        n = len(nums)
        prefix = [0] * n
        prefix_sum = 0
        for i in range(n):
            prefix_sum += nums[i] 
            prefix[i] = prefix_sum

        for i in range(n-l+1):
            total = 0
            for j in range(i+l-1,min(n, i+r)):
                if l<= j-i+1 <= r :
                    total = prefix[j] - (prefix[i - 1] if i > 0 else 0)
                    if total > 0:
                        mini = min(mini,total)
            
        return mini if mini != float("inf") else -1