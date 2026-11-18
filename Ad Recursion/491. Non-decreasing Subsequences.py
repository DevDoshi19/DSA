class Solution:
    def findSubsequences(self, nums: list[int]) -> list[list[int]]:
        ans = []
        n = len(nums)

        def solve(index, lst):
            if len(lst) >= 2:
                ans.append(lst.copy())

            used = set()

            for i in range(index, n):

                if nums[i] in used:
                    continue

                if lst and nums[i] < lst[-1]:
                    continue

                used.add(nums[i])

                lst.append(nums[i])
                solve(i + 1, lst)
                lst.pop()

        solve(0,[])
        return ans