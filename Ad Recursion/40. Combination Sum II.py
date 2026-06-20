from typing import List
class Solution:

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result: List[List[int]] = []

        def backtrack(index, total, path):
            if total == target:
                result.append(path.copy())
                return

            if index >= len(candidates) or total > target:
                return

            for i in range(index,len(candidates)) :
                if i > index and candidates[i] == candidates[i-1] :
                    continue 


                path.append(candidates[i])

                backtrack(
                    i + 1,total + candidates[i],path
                )   

                path.pop()

        backtrack(0, 0, [])

        return result