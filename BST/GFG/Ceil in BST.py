'''
Definition for Node
class Node:
    def __init__(self, val):
        self.right = None
        self.data = val
        self.left = None 
'''
        
class Solution:
    def findCeil(self,root, x):
        # code here
        celi = -1 
        
        while root : 
            if root.data == x :
                return root.data
                
            if x > root.data :
                root = root .right 
            
            else :
                celi = root.data 
                root = root.left
                
        return celi 
    

# t.c. = O(h) where h is the height of the tree
# or in avg case it is O(log n) and in worst case it is O(n) where n is the number of nodes in the tree

# s.c. = O(1) as we are not using any extra space