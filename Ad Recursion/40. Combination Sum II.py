from typing import List
class Solution:
    # this is a backtracking problem, we can use backtracking to solve this problem.

    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        result: List[List[int]] = []

        # simple steps : 
        # 1. we will use backtracking to find all the combinations of candidates that sum up to target.
        # 2. we will use a path list to keep track of the current combination.
        # 3. we will use a total variable to keep track of the current sum of the path.
        # 4. we will use an index variable to keep track of the current index in the candidates list.
        # 5. we will use a recursive function to explore all possible combinations.
        
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