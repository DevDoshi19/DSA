# https://www.geeksforgeeks.org/problems/subset-sum-problem-1611555638/1

# using recursion and backtracking
class Solution0:
    def isSubsetSum (self, arr, sum):
        # code here 
       # t.c. -> O(2^n) s.c. -> O(n)
        def backtrack(index,total):
            if total == sum :
                return True
                
            if index >= len(arr) or total > sum:
                return False 
             
            
            if  backtrack(index+1,total+arr[index]) or backtrack(index+1,total) :
                return True                
            
        if backtrack(0,0):
            return True
        return False 

# recursion + memoization
class Solution1:
    def isSubsetSum (self, arr, sum):
        # code here 

        # t.c. -> O(n*sum) s.c. -> O(n*sum)

        n = len(arr)
        dp = [[-1 for _ in range(sum+1)]for _ in range(n)]
        def backtrack(index,total,dp):
            if total == sum :
                return True
                
            if index >= len(arr) or total > sum:
                return False 
             
            if dp[index][total] != -1  :
                return dp[index][total]
            
            # if backtrack(index+1,total+arr[index],dp):
            #     dp[index][total] = True
            #     return True 
            # other way

            pick = backtrack(index+1,total+arr[index],dp)
            if pick :
                dp[index][total] = True
                return True
            
            not_pick = backtrack(index+1,total,dp)
            if not_pick :
                dp[index][total] = True
                return True 
                
            dp[index][total] = pick or not_pick
            return dp[index][total]
                
        if backtrack(0,0,dp):
            return True
        return False 
    
# a better recursion + memoization
class Solution1_1:
    def isSubsetSum (self, arr, sum):
        # code here 
        n = len(arr)
        dp = [[-1 for _ in range(sum+1)]for _ in range(n)]
        def backtrack(index,total,dp):
            if total == sum :
                return True
                
            if index >= len(arr) or total > sum:
                return False 
             
            if dp[index][total] != -1  :
                return dp[index][total]
            
            dp[index][total] = (
                backtrack(index+1, total+arr[index],dp) or
                backtrack(index+1, total,dp)
            )
            
            return dp[index][total]
                
        if backtrack(0,0,dp):
            return True
        return False 

# easy and better solution (Tabulation) 
class Solution3:
    def isSubsetSum (self, arr, sum):
        # code here 
        n = len(arr)
        dp = [[False for _ in range(sum+1)]for _ in range(n)]
        
        for i in range(n):
            dp[i][0] = True
       
        if arr[0] <= sum :
            dp[0][arr[0]] = True
           
        for index in range(1,n):
            for total in range(0,sum+1):
                if arr[index] > total :
                    pick = False
                else :
                    pick = dp[index-1][total-arr[index]]
                
                not_pick = dp[index-1][total]
                
                dp[index][total] = pick or not_pick 
                
        return dp[n-1][sum]
    
# T.c. = O(n*target)
# S.c. = O(2* target) ~ O(target)