# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        def dfs(node):
            if not node:
                return 0
            LH = dfs(node.left)
            if LH == -1:
                return -1
            RH = dfs(node.right)
            if RH == -1:
                return -1
            if abs(LH - RH) > 1 :
                return -1

            return max(LH,RH) + 1

        return dfs(root) != -1
    
class solution2:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        self.isbal = True
        
        def solve(node):
            # FIX 1: Must return 0 instead of None for an empty node
            if node is None:
                return 0
                
            LH = solve(node.left)
            RH = solve(node.right)
            
            # This is where your core balance check lives
            if abs(LH - RH) > 1:
                self.isbal = False 

            # FIX 2: Returns the correct calculation back up the tree
            return max(LH, RH) + 1

        solve(root)
        return self.isbal
