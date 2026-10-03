class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m > n :
            return -1
        
        for i in range(n-m+1):
            if haystack[i:i+m] == needle:
                return i

        return -1


# classical two pointer approach which is more efficient than the above approach
class Solution2:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m > n :
            return -1
        
        i = 0
        j = 0

        while i < n:
            if haystack[i] == needle[j]:
                i+=1
                j+=1
                if j == m :
                    return i-m
            else :
                i = i-j+1
                j = 0 

        return -1

# KMP algorithm approach
class Solution3:
    def strStr(self, haystack: str, needle: str) -> int:
        n = len(haystack)
        m = len(needle)
        if m > n :
            return -1
        
        LPS = [0] * m 
        i = 1 
        length = 0
        while i < m :
            if needle[i] == needle[length] :
                length += 1
                LPS[i] = length
                i+=1 
            else:
                if length > 0 :
                    length = LPS[length-1]
                else:
                    i += 1
        
        i = 0
        j = 0

        while i < n:
            if haystack[i] == needle[j]:
                i+=1
                j+=1
                if j == m :
                    return i-m
            else :
                if j != 0:
                    j = LPS[j-1]
                else:
                    i += 1

        return -1