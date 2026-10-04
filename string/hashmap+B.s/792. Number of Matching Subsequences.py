"""
792. Number of Matching Subsequences

Given a string s and an array of strings words, return the number of words[i] that is a subsequence of s.
A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.
For example, "ace" is a subsequence of "abcde".
 
Example 1:

Input: s = "abcde", words = ["a","bb","acd","ace"]
Output: 3
Explanation: There are three strings in words that are a subsequence of s: "a", "acd", "ace".

Example 2:

Input: s = "dsahjpjauf", words = ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
Output: 2
"""

# hashmap + binary search
from bisect import bisect_right 
class Solution:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:
        if not s :
            return 0

        mp : dict[str,list[int]] = {}
        for i,ch in enumerate(s):
            mp.setdefault(ch, []).append(i)
        
        count = 0
        for word in words :
            prev = -1 
            isValid = True
            for ch in word :
                if ch not in mp :
                    isValid = False 
                    break 
                
                indices = mp[ch]
                pos = bisect_right(indices,prev)

                if pos == len(indices):
                    isValid = False
                    break 
                
                prev = indices[pos]

            if isValid :
                count+=1
        
        return count
    
"""
Let:
- N = len(s)
- W = len(words) → number of words
- L = total number of characters across all words
- K = number of occurrences of the current character in s

t.c. = O(N + L * log K)
- O(N) to build the hashmap
- O(L * log K) to check each character in each word using binary search
s.c. = O(N + L)
- O(N) for the hashmap
- O(L) for the list of words
"""


# waiting list / buckets approach.
from collections import defaultdict, deque  # noqa: E402

class Solution2:
    def numMatchingSubseq(self, s: str, words: list[str]) -> int:

        waiting = defaultdict(deque)

        # Put every word into the bucket corresponding to its first character, which is form word
        for word in words:
            waiting[word[0]].append((word, 0))

        count = 0

        # Scan s only once
        for ch in s:
            current = waiting[ch] # Process everyone waiting for this character
            size = len(current)

            for _ in range(size):
                word, index = current.popleft()

                index += 1
                if index == len(word): # Word completely matched
                    count += 1

                else:
                    # Wait for the next character
                    next_ch = word[index]
                    waiting[next_ch].append((word, index))

        return count