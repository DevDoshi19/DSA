"""
1392. Longest Happy Prefix

A string is called a happy prefix if it is a non-empty prefix which is also a suffix (excluding itself).

Given a string s, return the longest happy prefix of s. Return an empty string "" if no such prefix exists.

"""

class Solution:
    def longestPrefix(self, s: str) -> str:
        n = len(s)
        LPS = [0] * n 
        i = 1 
        length = 0
        while i < n :
            if s[i] == s[length] :
                length += 1
                LPS[i] = length
                i+=1 
            else:
                if length > 0 :
                    length = LPS[length-1]
                else:
                    i += 1
        
        return s[:LPS[-1]]
    
# longest happy prefix is the longest prefix which is also a suffix. The above code uses KMP algorithm to find the longest happy prefix. The LPS array is used to store the length of the longest prefix which is also a suffix for each substring of the given string. The final answer is the substring from the start of the string to the length of the longest happy prefix found in the LPS array.
# t.c. = O(n) and s.c. = O(n)
