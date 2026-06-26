from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        stack = []
        ans = [0] *n
        for i in range(n):
            while stack and temperatures[stack[-1]] < temperatures[i] :
                ind = stack.pop()
                ans[ind] = i - ind
            stack.append(i)
        return ans