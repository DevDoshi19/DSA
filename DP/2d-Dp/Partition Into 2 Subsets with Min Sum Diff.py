class Solution:
    def minDifference(self, arr: list[int]) -> int:
        # code here
        total = sum(arr)
        n = len(arr)
        dp = [[False for _ in range(total+1)]for _ in range(n)]

        for i in range(n):
            dp[i][0] = True
        if arr[0] < total :
            dp[0][arr[0]] = True
            
        for index in range(1, n):
            for target in range(0, total + 1):
                if arr[index] > target :
                    pick = False
                else:
                    pick= dp[index][target-arr[index]]
                
                not_pick = dp[index-1][target]
                dp[index][target] = pick or not_pick
                    
        mini = float("inf")
        for s1 in range(total+1):
            if dp[n-1][s1] is True :
                s2 =abs(total - s1)
                mini = min(mini,abs(s1-s2))
                
        return mini