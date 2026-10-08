class Solution:
    def shortestPalindrome(self, s: str) -> str:
        if not s:
            return ""
            
        n = len(s)
        rev = s[::-1]
        new_s = s + "#" + rev 
        
        m = len(new_s)
        LPS = [0] * m 
        length = 0 
        i = 1

        while i < m :
            if new_s[i] == new_s[length] :
                length += 1
                LPS[i]= length
                i += 1

            else :
                if length <= 0:
                    LPS[i] = 0 
                    i += 1
                else: 
                    length = LPS[length-1]

        index = LPS[m-1]
        return rev[0:n-index]+s