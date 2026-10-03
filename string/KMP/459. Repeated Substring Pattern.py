"""
459. Repeated Substring Pattern
Solved
Easy
Topics
premium lock icon
Companies
Given a string s, check if it can be constructed by taking a substring of it and appending multiple copies of the substring together.

 

Example 1:

Input: s = "abab"
Output: true
Explanation: It is the substring "ab" twice.
Example 2:

Input: s = "aba"
Output: false
Example 3:

Input: s = "abcabcabcabc"
Output: true
Explanation: It is the substring "abc" four times or the substring "abcabc" twice.
 

Constraints:

1 <= s.length <= 104
s consists of lowercase English letters.
"""

class Solution:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        LPS = [0] *n
        i = 1
        length = 0
        while i <n:
            if s[i] == s[length]:
                length +=1
                LPS[i] = length
                i+= 1
            else :
                if length > 0:
                    length = LPS[length-1]
                else:
                    i+=1
        
        pattern_length = n - LPS[-1]

        return LPS[-1] > 0 and n % pattern_length == 0
    
# brute force approach is to check for all possible substring lengths from 1 to n//2 and see if the string can be formed by repeating the substring. The above code uses KMP algorithm to find the longest prefix which is also a suffix. If the length of the longest prefix which is also a suffix is greater than 0 and the length of the string is divisible by the length of the pattern, then the string can be formed by repeating the substring. The time complexity is O(n) and space complexity is O(n).
class Solution2:
    def repeatedSubstringPattern(self, s: str) -> bool:
        n = len(s)
        for i in range(1, n//2 + 1):
            if n % i == 0:
                if s[:i] * (n // i) == s:
                    return True
        return False
    
class Solution3:
    def repeatedSubstringPattern(self, s: str) -> bool:
        
        s_fold = "".join( (s[1:], s[:-1]) )
        
        return s in s_fold