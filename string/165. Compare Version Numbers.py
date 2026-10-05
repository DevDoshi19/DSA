"""
Given two version strings, version1 and version2, compare them. A version string consists of revisions separated by dots '.'. The value of the revision is its integer conversion ignoring leading zeros.
To compare version strings, compare their revision values in left-to-right order. If one of the version strings has fewer revisions, treat the missing revision values as 0.

Return the following:
If version1 < version2, return -1.
If version1 > version2, return 1.
Otherwise, return 0.
 
Example 1:
Input: version1 = "1.2", version2 = "1.10"
Output: -1
Explanation:
version1's second revision is "2" and version2's second revision is "10": 2 < 10, so version1 < version2.

Example 2:
Input: version1 = "1.01", version2 = "1.001"
Output: 0
Explanation:
Ignoring leading zeroes, both "01" and "001" represent the same integer "1".

Example 3:
Input: version1 = "1.0", version2 = "1.0.0.0"
Output: 0
Explanation:
version1 has less revisions, which means every missing revision are treated as "0".
"""

class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        # Time: O(n + m)
        # Space: O(n + m)

        num1 = []
        word = ""
        for ch in version1:
            if ch == ".":
                num1.append(int(word))
                word = ""
            else:
                word += ch
        
        num1.append(int(word))

        num2 = []
        word = ""
        for ch in version2:
            if ch == ".":
                num2.append(int(word))
                word = ""
            else:
                word += ch
        num2.append(int(word))
            
        while len(num1) < len(num2):
            num1.append(0)

        while len(num2) < len(num1):
            num2.append(0)

        if num1 == num2:
            return 0
        
        if num1 > num2 :
            return 1
        
        return -1
    
# apporch 2 : using 2 pointer just to imporve the space complexity into 0(1)

# Time: O(n + m)
# Extra space: O(1)
class Solution2:
    def compareVersion(self, version1: str, version2: str) -> int:
        i = 0
        j = 0

        n = len(version1)
        m = len(version2)

        while i < n or j < m:

            start1 = i
            while i < n and version1[i] != ".":
                i += 1

            start2 = j
            while j < m and version2[j] != ".":
                j += 1

            val1 = int(version1[start1:i]) if start1 < i else 0
            val2 = int(version2[start2:j]) if start2 < j else 0

            if val1 > val2:
                return 1

            if val1 < val2:
                return -1

            if i < n:
                i += 1

            if j < m:
                j += 1

        return 0