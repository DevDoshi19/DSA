class Solution:
    def maximumSubarraySum(self, nums: list[int], k: int) -> int:
        mp = {}
        current_sum = 0
        maxi = 0
        i = 0

        for j in range(len(nums)):
           
            current_sum += nums[j]
            mp[nums[j]] = mp.get(nums[j], 0) + 1

            if j - i + 1 > k:
                mp[nums[i]] -= 1
                current_sum -= nums[i]

                if mp[nums[i]] == 0:
                    del mp[nums[i]]

                i += 1

            if j - i + 1 == k and len(mp) == k:
                maxi = max(maxi, current_sum)

        return maxi