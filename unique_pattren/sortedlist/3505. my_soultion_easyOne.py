from typing import List

from sortedcontainers import SortedList # pyright: ignore[reportMissingImports]
class Window:
    def __init__(self,arr,x):
        self.x = x 
        m = (self.x+1) // 2 
        
        init_arr = SortedList(arr)
        self.smaller = SortedList(init_arr[:m])
        self.larger = SortedList(init_arr[m:])

        self.sumSmaller = sum(self.smaller)
        self.sumLarger = sum(self.larger)

        self.median = self.smaller[-1]    
    
    def add(self,val):
        if val > self.median :
            self.sumLarger += val
            self.larger.add(val)
        else:
            self.sumSmaller += val
            self.smaller.add(val)
        
    def remove(self,val):
        if val <= self.median :
            self.smaller.remove(val)
            self.sumSmaller -= val
        else:
            self.larger.remove(val)
            self.sumLarger -= val


    def rebalance(self):
        target = (self.x + 1) // 2

        while len(self.smaller) > target:
            ele = self.smaller.pop()
            self.sumSmaller -= ele
            self.larger.add(ele)
            self.sumLarger += ele

        while len(self.smaller) < target:
            ele = self.larger.pop(0)
            self.sumLarger -= ele
            self.smaller.add(ele)
            self.sumSmaller += ele

        self.median = self.smaller[-1]

    def cost(self):
        return (self.median*len(self.smaller)-self.sumSmaller) + (self.sumLarger - (self.median*len(self.larger)))
            

class Solution:
    def minOperations(self, nums: List[int], x: int, k: int) -> int:
        window = Window(nums[:x],x)
        window.rebalance()

        n = len(nums)
        cost = [0] * (n-x+1)
        cost[0] = window.cost()

        for i in range(x,n):
            window.remove(nums[i-x])
            window.add(nums[i])
            window.rebalance()
            cost[i-x+1] = window.cost()

        INF = float("inf")
        dp = [[INF for _ in range(n+1)] for _ in range(k+1)]

        for i in range(n+1):
            dp[0][i] = 0
        
        for j in range(1,k+1):
            for i in range(1,n+1):

                dp[j][i] = dp[j][i-1]

                if i >= x :
                    dp[j][i] = min(
                                dp[j][i-1],
                                dp[j-1][i-x] + cost[i-x]
                            )

        return dp[k][n]        
