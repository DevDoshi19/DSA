"""
You are given two integers n and t. 
Return the smallest number greater than or equal to n such that the product of its digits is divisible by t.

Example 1:

Input: n = 10, t = 2

Output: 10

Explanation:

The digit product of 10 is 0, which is divisible by 2, 
making it the smallest number greater than or equal to 10 that satisfies the condition.

"""

class Solution:
    def get_product(self,number):
        product = 1
        while number>0:
            digit = number % 10
            product *= digit
            number //= 10

        return product

    def smallestNumber(self, n: int, t: int) -> int:
        candidate = n 

        while True :
            if self.get_product(candidate) % t == 0 :
                return candidate
            candidate += 1