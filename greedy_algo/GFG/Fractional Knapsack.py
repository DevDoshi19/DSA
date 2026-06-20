class Solution:
    def fractionalKnapsack(self, val, wt, capacity):
        #code here
        arr = []
        for i in range(len(wt)):
            arr.append([val[i],wt[i]])
            
        arr.sort(key=lambda x:x[0]/x[1] , reverse=True)
        max_val = 0
        
        for v ,w in arr :
            diff = capacity - w
            if diff >= 0:
                max_val += v 
                capacity -= w
            
            else :
                cap = (v/w) * capacity
                max_val += cap
                break
            
        return max_val
    
