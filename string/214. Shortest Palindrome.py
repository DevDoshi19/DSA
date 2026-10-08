class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # brute force solution where we are comparing the string with its reverse
        # if we found that the string is not a palindrome then we will add the reverse of the string to the front of the string and return it
        # if the string is a palindrome then we will return the string as it is

        # t.c. O(n^2) and s.c. O(n)

        new_s = ""
        m = len(s)
        for i in range(m-1,-1,-1):
            st = s[0:i+1] 
            if st == st[::-1]:
                return new_s + s
            else:
                new_s += s[i]


        return new_s+s