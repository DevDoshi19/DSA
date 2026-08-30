from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        maxi = max(strs)
        mini = min(strs)
        
        n = len(maxi)
        m = len(mini)

        i = 0
        while i < n and i <m :
            if maxi[i] == mini[i] :
                prefix += maxi[i]
            else :
                return prefix
            
            i+=1 

        return prefix