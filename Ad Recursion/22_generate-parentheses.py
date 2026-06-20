from typing import List
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        bracket =[""] * n*2
        def backtrack(index,total):
            if index >= len(bracket):
                if total == 0 :
                    result.append("".join(bracket))
                return

            if total > (len(bracket)//2):
                return
            elif total < 0 :
                return

            bracket[index] = "("
            sum = total + 1

            backtrack(index+1,sum)
            
            bracket[index] = ")"
            sum = total - 1
            backtrack(index+1,sum)

        return backtrack(0,0)