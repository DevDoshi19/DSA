from collections import deque

class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None

# the t.c. : O(N + NlogN + N ) 
# The s.c. : O(N + N) 

class Solution:
    def topView(self, root):
        # code here
        queue = deque()
        ans = []
        res = {}
        
        if root is None:
            return None

        queue.append((root,0))
        
        while len(queue) != 0 :
            e,line = queue.popleft()
            
            res[line] = e.data
                
            if e.left :
                queue.append((e.left,line-1))
            if e.right :
                queue.append((e.right,line+1))
                
            
        for val in sorted(res.items()):
            ans.append(val[1])
            
        return ans