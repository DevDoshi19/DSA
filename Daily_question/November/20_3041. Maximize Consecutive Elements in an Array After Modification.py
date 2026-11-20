class Solution:
    def maxSelectedElements(self, nums: list[int]) -> int:
        nums.sort()
        dp: dict[int, int] = {}
        max_len = 0

        for x in nums:
            v1 = dp.get(x, 0) + 1
            v2 = dp.get(x - 1, 0) + 1

            dp[x + 1] = max(dp.get(x + 1, 0), v1)
            dp[x] = max(dp.get(x, 0), v2)

            max_len = max(max_len, dp[x + 1], dp[x])

        return max_len