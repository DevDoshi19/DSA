from typing import List
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        char_map = {"1":"","2":"abc","3":"def","4":"ghi","5":"jkl","6":"mno","7":"pqrs","8":"tuv","9":"wxyz"}
        result: List[str] = []
        def solve(index,lst):

            if index >= len(digits):
                result.append("".join(lst.copy()))
                return

            for ch in char_map[digits[index]]:
                lst.append(ch)
                solve(index+1,lst)
                lst.pop()

        solve(0,[])
        return result 