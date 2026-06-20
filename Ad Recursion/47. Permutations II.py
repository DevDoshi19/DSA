from typing import List
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        result = []
        used = [False]* len(nums)
        def backtrack(path):
            if len(path) == len(nums):
                result.append(path.copy())
                return 

            for i in range(len(nums)):
                if i>0 and nums[i] == nums[i-1] and not used[i-1] :
                    continue
                elif used[i] == True :
                    continue
                else:
                    used[i] = True
                    path.append(nums[i])
                    backtrack(path)

                    used[i] = False
                    path.pop()

        backtrack([])
        return result