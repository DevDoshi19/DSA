from ast import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result = []
        bracket = []
        # t.c. = O(2** 2n) , s.c. = O(2n)
        def solve(index,open,close,bracket):
            if index >= n*2: 
                # if open == n and close == n :
                result.append("".join(bracket))
                return  
            
            if open < n :
                bracket.append("(")
                solve(index+1,open+1,close,bracket)
                bracket.pop()

            if close < open :
                bracket.append(")")
                solve(index+1,open,close+1,bracket)
                bracket.pop()

        solve(0,0,0,bracket)

        return result