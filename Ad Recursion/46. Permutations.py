from typing import List
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        used = [False]*len(nums)
        result = []

        def backtrack(index,path):
            if len(path) == len(nums):
                result.append(path.copy())
                return 

            for i in range(len(nums)):

                if used[i]:
                    continue
                else:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(i+1,path)

                    path.pop()
                    used[i]=False

        backtrack(0,[])

        return result

nums = [1,2,3]
s = Solution()
print(s.permute(nums))