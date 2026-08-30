class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        count = 0 
        result = ""

        for ch in s :
            if ch == "(":
                count += 1
            if ch == ")":
                count -= 1 

            if count > 1 and ch == "(":
                result += ch 
            if count > 0 and ch == ")":
                result += ch 

        return result 