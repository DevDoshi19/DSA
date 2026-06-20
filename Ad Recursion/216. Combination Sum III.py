from typing import List
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        result: List[List[int]] = []
        lst: List[int] = []
        def backtrack(start_number,remening_number,lst):
            if remening_number == 0 and len(lst) == k:
                result.append(lst.copy())
                return
            if remening_number < 0 :
                return

            if len(lst) > k :
                return

            for i in range(start_number,10):
                number = remening_number - i
                lst.append(i)
                backtrack(i+1,number,lst)
                e = lst.pop()


        backtrack(1,n,[])
        return result
        