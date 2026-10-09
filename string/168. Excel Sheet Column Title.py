class Solution:
    # Time: O(log_{26} N), where (N) is columnNumber.
    # Space: O(log_{26} N) to store the output characters.

    def convertToTitle(self, columnNumber: int) -> str:
        
        if 1 <=columnNumber <= 26 :
            return chr(64+columnNumber) 
        
        ans = []
        while columnNumber > 0 :
            columnNumber -= 1
            num = int(columnNumber % 26) 
            columnNumber //= 26  
            ans.append(chr(65+num))

        return "".join(ans[::-1])

"""
Step 1: Find the rightmost character
\[
701-1=700
\]

\[
700\bmod26=24
\]

Since A corresponds to 0 after the adjustment, 24 corresponds to Y.
Collected: Y

Step 2: Remove that character's place
\[
700//26=26
\]

Process the remaining number:
\[
26-1=25
\]

\[
25\bmod26=25
\]


25 corresponds to Z.
Collected: Y, Z

Step 3: Finish

26//26=1


After the next iteration, the number becomes zero and the loop ends.
Collected characters: YZ
Final answer after reversing: ZY
"""