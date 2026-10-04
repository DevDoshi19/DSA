# 392. Is Subsequence
'''
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).

Example 1:
Input: s = "abc", t = "ahbgdc"
Output: true

Example 2:
Input: s = "axc", t = "ahbgdc"
Output: false 
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i,j=0,0
        n,m=len(s),len(t)

        if not s:
            return True

        if n > m or not t:
            return False

        while j < m :
            if s[i] == t[j] :
                i+=1
                j+=1
                if i == n :
                    return True 
            else:
                j+=1 

        return False 
    
# Follow up: Suppose there are lots of incoming s, say s1, s2, ..., sk where k >= 109, and you want to check one by one to see if t has its subsequence. In this scenario, how would you change your code?

from bisect import bisect_right  # noqa: E402

class Solution2:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)

        # Preprocess t so we don't need to recalculate t everytime ( follow up question )
        mp: dict[str, list[int]] = {}
        for i in range(m):
            if t[i] in mp:
                mp[t[i]].append(i)
            else:
                mp[t[i]] = [i]

        prev = -1
        # Processing s 
        for i in range(n):
            ch = s[i]

            if ch not in mp:
                return False

            indices = mp[ch]
            pos = bisect_right(indices, prev)
            if pos == len(indices):
                return False

            prev = indices[pos]

        return True
    
# steps : 
# 1. Preprocess t and store the indices of each character in a dictionary.
# 2. For each character in s, use binary search to find the next index in t that is greater than the previous index found.
# 3. If we can't find a valid index for any character in s, return False. Otherwise, return True after processing all characters in s.