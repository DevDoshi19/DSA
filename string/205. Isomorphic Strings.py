class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False 

        freq_s = {}
        freq_t = {}
        n = len(s)
        for i in range(n):
            if s[i] in freq_s and freq_s[s[i]] != t[i]:
                return False 
                
            if t[i] in freq_t and freq_t[t[i]] != s[i]:
                return False
        
            freq_s[s[i]] = t[i]
            freq_t[t[i]] = s[i]

        return True