"""
We build a table of n rows (1-indexed). We start by writing 0 in the 1st row. Now in every subsequent row, we look at the previous row and replace each occurrence of 0 with 01, and each occurrence of 1 with 10.

For example, for n = 3, the 1st row is 0, the 2nd row is 01, and the 3rd row is 0110.
Given two integer n and k, return the kth (1-indexed) symbol in the nth row of a table of n rows.

Example 1:

Input: n = 1, k = 1
Output: 0
Explanation: row 1: 0


Time complexity: O(n), because each recursive call reduces n by one.

Auxiliary space: O(n), because of the recursion call stack.

"""

class Solution:
    def kthGrammar(self, n: int, k: int) -> int:
        if n == 1 and k == 1:
            return 0 
        
        length = pow(2,n-1) 
        mid = length // 2 

        if k <= mid :
            return self.kthGrammar(n-1,k)
        else:
            return 1-self.kthGrammar(n-1,k-mid)