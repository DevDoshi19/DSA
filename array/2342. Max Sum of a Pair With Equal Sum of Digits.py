'''
2342. Max Sum of a Pair With Equal Sum of Digits
You are given a 0-indexed array nums consisting of positive integers. You can choose two indices i and j, such that i != j, and the sum of digits of the number nums[i] is equal to that of nums[j].

Return the maximum value of nums[i] + nums[j] that you can obtain over all possible indices i and j that satisfy the conditions. If no such pair of indices exists, return -1.
 
Example 1:
Input: nums = [18,43,36,13,7]
Output: 54
Explanation: The pairs (i, j) that satisfy the conditions are:
- (0, 2), both numbers have a sum of digits equal to 9, and their sum is 18 + 36 = 54.
- (1, 4), both numbers have a sum of digits equal to 7, and their sum is 43 + 7 = 50.
So the maximum sum that we can obtain is 54.

Example 2:
Input: nums = [10,12,19,14]
Output: -1
Explanation: There are no two numbers that satisfy the conditions, so we return -1.
'''
class Solution:
    def maximumSum(self, nums: list[int]) -> int:
        digit_sum = {}
        result = -1
        
        for num in nums:
            total = 0
            temp = num
            while temp > 0:
                total += temp % 10
                temp //= 10
            
            if total in digit_sum:
                result = max(result, digit_sum[total] + num)
                if num > digit_sum[total]:
                    digit_sum[total] = num
            else:
                digit_sum[total] = num

        return result

class Solution2:
    def maximumSum(self, nums: list[int]) -> int:
        # approch 2 - constant space ( highest sum = 81 ( 10**9 = 9+9+9+...+9 (9 times) = 81)) 
        n = len(nums)
        digit_sum = [0] * 82
        result = -1
        for i in range(n):
            j = nums[i]
            total = sum(int(d) for d in str(j))

            if digit_sum[total] != 0 :
                result = max(result,digit_sum[total] + nums[i])
                digit_sum[total]= max(digit_sum[total],nums[i])
            else:
                digit_sum[total] = nums[i]
                

        return result