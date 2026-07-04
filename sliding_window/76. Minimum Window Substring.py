from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not t or not s :
            return ""
        
        freq2 = Counter(t)
        freq = {}

        need = len(freq2)
        have = 0

        left = 0 
        result = ""
        min_len = float("inf")

        for right in range(len(s)):
            char = s[right]
            freq[char] = freq.get(char,0)+1

            if char in freq2 and freq[char] == freq2[char]:
                have +=1 

            while have == need :
                
                if (right - left+1) < min_len :
                    min_len = right - left + 1
                    result = s[left:right+1]

                left_char = s[left]
                freq[left_char] -= 1
                if left_char in freq2 and freq[left_char] < freq2[left_char]:
                    have -=1 
                left +=1

        return result