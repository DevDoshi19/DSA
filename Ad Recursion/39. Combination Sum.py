from typing import List
class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        lst= List[int]
        
        def solve(index,total,lst):
            if total == target :
                result.append(lst.copy())
                return 
            if index >= len(candidates):
                return 

            if total > target :
                return 

        
            lst.append(candidates[index])
            solve(index,total + candidates[index],lst) 
        
            lst.pop()
            solve(index+1,total,lst)

        solve(0,0,[])

        return result
        