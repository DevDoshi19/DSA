# a really goof question to solve using recursion and backtracking
"""
You are given an array of strings arr. A string s is formed by the concatenation of a subsequence of arr that has unique characters.

Return the maximum possible length of s.

A subsequence is an array that can be derived from another array by deleting some or no elements without changing the order of the remaining elements.

 

Example 1:

Input: arr = ["un","iq","ue"]
Output: 4
Explanation: All the valid concatenations are:
- ""
- "un"
- "iq"
- "ue"
- "uniq" ("un" + "iq")
- "ique" ("iq" + "ue")
Maximum length is 4.
Example 2:

Input: arr = ["cha","r","act","ers"]
Output: 6
Explanation: Possible longest valid concatenations are "chaers" ("cha" + "ers") and "acters" ("act" + "ers").
Example 3:

Input: arr = ["abcdefghijklmnopqrstuvwxyz"]
Output: 26
Explanation: The only string in arr has all 26 characters.
 

Constraints:

1 <= arr.length <= 16
1 <= arr[i].length <= 26
arr[i] contains only lowercase English letters.
"""

class Solution:
    def maxLength(self, arr: list[str]) -> int:
        n =len(arr)
        self.maxi = 0

        def backtrack(index,temp):
            self.maxi = max(self.maxi,len(temp))

            if index == n :
                return 

            for i in range(index,n) :
                curr = temp
                candidate = arr[i]
                if len(set(candidate)) != len(candidate) :
                    continue

                valid = True
                for c in candidate :
                    if c in temp :
                        valid = False
                        break

                if not valid:
                    continue

                temp += candidate
                backtrack(i+1,temp)
                temp = curr
                            
        backtrack(0,"")
        return self.maxi

"""
1. Time Complexity
Your recursion explores combinations of strings.

For every string, we have two possibilities:
- Include it.
- Exclude it.
Therefore, the number of possible subsets is:  2^n


For each candidate, you perform:
- set(candidate) → O(m)
- Checking characters against temp → O(m * n * m) in the worst case if temp is checked using a Python string.
More precisely, c in temp takes O(nm) in the worst case.

Thus, a safe upper bound for your implementation is:
O(2^n * n * m)

Your proposed O(2^n * m) misses the cost of checking membership in temp.
2. Space Complexity
- Recursion depth: O(n)
- Current concatenated string: O(nm)
- Temporary set: O(m)
Therefore: O(nm)


This is auxiliary space, excluding the input and output.
Final interview answer
Complexity	Answer
Time	O(2^n * n * m)
Auxiliary Space	O(nm)
"""