"""
Definition for Node
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
"""

class Solution:
    def minValue(self, root):
        # code here
        curr = root 
        
        if root is None :
            return -1
        if root.left is None:
            return root.data
        
        mini = float("-inf")
        
        while curr :
            mini = curr.data
            curr =curr.left
            
        return mini