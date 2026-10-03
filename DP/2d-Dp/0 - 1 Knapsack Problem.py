class Solution:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        # code here
        n = len(val)
        dp = [[-1 for _ in range(W+1)]for _ in range(n)]
        def backtrack(index,weight):
            if index == 0:
                if wt[index] <= weight:
                    return val[index]
                return 0 
            
            if dp[index][weight] != -1 : 
                return dp[index][weight]
            
            if wt[index] > weight :
                pick = float("-inf")
            else:
                pick = val[index]+backtrack(index-1,weight-wt[index])
            
            not_pick = backtrack(index-1,weight)
            dp[index][weight] = max(pick,not_pick)
            
            return dp[index][weight]
            
        return backtrack(n-1,W)
        
# tabulation
class Solution2:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        # code here
        n = len(val)
        dp = [[0 for _ in range(W+1)]for _ in range(n)]
        for w in range(0,W+1):
            if wt[0] <= w:
                dp[0][w] = val[0]

        for index in range(1,n):
            for weight in range(W+1):
                if wt[index] > weight :
                    pick = float("-inf")
                else:
                    pick = val[index] + dp[index-1][weight - wt[index]]
                not_pick = dp[index-1][weight]
                
                dp[index][weight] = max(pick,not_pick)
            
        return dp[n-1][W]

# space optimization   
class Solution3:
    def knapsack(self, W: int, val: list[int], wt: list[int]) -> int:
        # code here
        n = len(val)
        prev = [0 for _ in range(W+1)]
        for w in range(0,W+1):
            if wt[0] <= w:
                prev[w] = val[0]

        for index in range(1,n):
            curr = [0 for _ in range(W+1)]
            for weight in range(W+1):
                if wt[index] > weight :
                    pick = float("-inf")
                else:
                    pick = val[index] + prev[weight - wt[index]]
                not_pick = prev[weight]
                
                curr[weight] = max(pick,not_pick)
            
            prev = curr
            
        return prev[W]