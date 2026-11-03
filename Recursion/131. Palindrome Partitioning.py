from typing import List
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        def isPalindrome(st):
            return st == st[::-1] 
        
        def backtrack(index,st):
            if index == len(s):
                result.append(st.copy())
                return

            for i in range(index,len(s)):
                ch = s[index:i+1]
                if isPalindrome(ch):
                    st.append(ch)
                    backtrack(i+1,st)
                    st.pop()
        
        backtrack(0,[])
        return result
    
"""
Worst-case time: O(n * 2^n) with palindrome checking included.
Auxiliary space: O(n) for recursion and the current partition.

Remember this pattern:

For partitioning problems:
for i in range(index, len(s)):    
    ch = s[index:i+1]

The current index tells you where the next substring must begin.
"""