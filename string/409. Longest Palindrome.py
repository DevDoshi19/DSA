from collections import Counter

# T.c = O(n) , s.c. = O(k) 
#  0(n) = we are iterating through the string to get the frequency of each character and then we are iterating through the frequency dictionary to get the count of characters that can be used to form a palindrome.
# counter take O(k) alpha betic space to store the frequency of each character in the string. and t.c. is also O(n) to iterate through the frequency dictionary to get the count of characters that can be used to form a palindrome.

class Solution:
    def longestPalindrome(self, s: str) -> int:
        freq = Counter(s)

        count = 0
        isSingle = False

        for value in freq.values():
            if value % 2 == 0:
                count += value
            else:
                count += value - 1
                isSingle = True

        return count + 1 if isSingle else count