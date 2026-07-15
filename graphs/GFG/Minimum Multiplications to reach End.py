from collections import deque
class Solution:
    def minSteps(self, arr, start, end):
        # code here
        queue = deque()
        dist = [float("inf")] * 1000
        dist[start] = 0
        
        queue.append((0,start))
        
        while len(queue) != 0 :
            step,num = queue.popleft()
            
            if num == end :
                return step
            
            for val in arr :
                new_v = (val * num) %1000
                if step+ 1 < dist[new_v] :
                    dist[new_v] = step+1
                    queue.append((step+1,new_v))
                
        return -1