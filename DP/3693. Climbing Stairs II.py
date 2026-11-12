from typing import List


class Solution:
    def climbStairs(self, n: int, costs: List[int]) -> int:
        dp = [float("inf")] * (n + 1)
        dp[0] = 0

        for i in range(1, n + 1):

            for jump in range(1, 4):
                prev = i - jump

                if prev >= 0:
                    current_cost = costs[i - 1] + jump ** 2
                    dp[i] = min(dp[i], dp[prev] + current_cost)

        return dp[n]