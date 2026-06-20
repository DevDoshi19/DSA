class Solution:
    def findMin(self, n):
       # code here 
        coin = [10,5,2,1]
        i = 0
        total = 0
        while n != 0 :
            if (n // coin[i]) > 0 :
                total += (n//coin[i])
                n = n - coin[i]*(n//coin[i])
            else :
                i+=1
                
        return total 

