# https://www.geeksforgeeks.org/problems/perfect-sum-problem5633/1

"""
Count Subsets with Sum
Solved
Difficulty: MediumAccuracy: 20.58%Submissions: 676K+Points: 4
Given an array arr[] of non-negative integers and an integer target, the task is to count all subsets of the array whose sum is equal to the given target.

Examples:

Input: arr[] = [5, 2, 3, 10, 6, 8], target = 10
Output: 3
Explanation: The subsets {5, 2, 3}, {2, 8}, and {10} sum up to the target 10.
Input: arr[] = [2, 5, 1, 4, 3], target = 10
Output: 3
Explanation: The subsets {2, 1, 4, 3}, {5, 1, 4}, and {2, 5, 3} sum up to the target 10.
Input: arr[] = [5, 7, 8], target = 3
Output: 0
Explanation: There are no subsets of the array that sum up to the target 3.
"""

class Solution:
    def perfectSum(self, arr, n, sum):
        n = len(arr)
        def backtrack(index,total):
            if total == sum:
                return 1
            if index >= n or total > sum:
                return 0

            include = backtrack(index+1,total+arr[index])
            exclude = backtrack(index+1,total)

            return include + exclude
        
        return backtrack(0,0)
    
# using DP in recursion
class Solution1:
    def perfectSum(self, arr, n, sum):
        dp = [[-1 for j in range(sum+1)] for i in range(n+1)]

        def backtrack(index,total):
            if total == sum:
                return 1
            if index >= n or total > sum:
                return 0

            if dp[index][total] != -1:
                return dp[index][total]

            include = backtrack(index+1,total+arr[index])
            exclude = backtrack(index+1,total)

            dp[index][total] = include + exclude
            return dp[index][total]
        
        return backtrack(0,0)

# using DP with space optimization 
class Solution2:
    def perfectSum(self, arr, n, sum):
        dp = [[0 for j in range(sum+1)] for i in range(n+1)]

        for i in range(n+1):
            dp[i][0] = 1

        for i in range(1,n+1):
            for j in range(1,sum+1):
                if arr[i-1] <= j:
                    dp[i][j] = dp[i-1][j-arr[i-1]] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]

        return dp[n][sum]
		# code here

# backword recursion	
class Solution3:
    def solve(self, index, total, arr):
        # Base case at first element (handle zero carefully)
        if index == 0:
            if total == 0 and arr == 0:
                return 2
            if total == 0 or arr == total:
                return 1
            return 0
        # Try pick if feasible, else 0
        if arr[index] > total:
            pick = 0
        else:
            pick = self.solve(index - 1, total - arr[index], arr)
        # Not pick path
        not_pick = self.solve(index - 1, total, arr)
        # Total ways = pick + not_pick
        return pick + not_pick

    def perfectSum(self, arr, target):
        n = len(arr)
        return self.solve(n - 1, target, arr)
    
# tabulation
class Solution4:
    def perfectSum(self, arr, target):
        n = len(arr)
        # create a 2D dp array with 0 initialized because if we don't find any subset with sum equal to target, we will return 0
        dp = [[0] * (target + 1) for _ in range(n)]

        if arr[0] == 0:
            dp[0][0] = 2
        else:
            dp[0][0] = 1
            if arr[0] <= target:
                dp[0][arr[0]] = 1

        for index in range(1, n):
            for total in range(target + 1):
                not_pick = dp[index - 1][total]
                pick = 0
                if arr[index] <= total:
                    pick = dp[index - 1][total - arr[index]]
                dp[index][total] = pick + not_pick

        return dp[n - 1][target]   

# tabulation with space optimization
class Solution5:
    def perfectSum(self, arr, target):
        n = len(arr)
        prev = [0 for _ in range(target + 1)] 

        if arr[0] == 0:
            prev[0] = 2
        else:
            prev[0] = 1
            if arr[0] <= target:
                prev[arr[0]] = 1

        for index in range(1, n):
            curr = [0 for _ in range(target + 1)]
            for total in range(target + 1):
                not_pick = prev[total]
                pick = 0
                if arr[index] <= total:
                    pick = prev[total - arr[index]]
                curr[total] = pick + not_pick
            prev = curr
    
        return prev[target]   