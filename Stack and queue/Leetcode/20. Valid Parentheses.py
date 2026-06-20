class Solution:
    def isValid(self, s: str) -> bool:
        if len(s) <=1:
            return False

        stack = []
        mapping = {')':'(', '}':'{',']':'['}

        for char in s :
            if char in mapping.values() :
                stack.append(char)
            elif char in mapping.keys():
                if not stack or mapping[char] != stack.pop():
                    return False
            
        return not stack                
    
# solution 2 : which is more efficient than solution 1 because it uses less space by not storing the mapping in a dictionary and instead using a simple if condition to check for pairs.
class Solution1:
    def isPair(self,top,curr):
        if top == "(" and curr == ")" or  top == "{" and curr == "}" or  top == "[" and curr == "]" :
            return True
        return False
    def isValid(self, s: str) -> bool:
        if len(s) <=1:
            return False

        stack = []
        for i in range(len(s)) :
            if stack :
                last = stack[-1]
                if self.isPair(last,s[i]):
                    stack.pop()
                    continue

            stack.append(s[i])

        return not stack                