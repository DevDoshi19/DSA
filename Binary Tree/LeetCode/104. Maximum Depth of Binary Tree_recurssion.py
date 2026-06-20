# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    # t.c O(n) where n is the number of nodes in the tree
    # s.c O(n) where n is the number of nodes in the tree
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        max_depth = 0 
        ele = []
        def depth(node):
            nonlocal max_depth
            if node is None :
                max_depth = max(max_depth,len(ele))
                return 

            ele.append(node.val) 
            depth(node.left)
            depth(node.right) 
            ele.pop() 

        depth(root)

        return max_depth
        
class Solution2:
    def maxDepth(self, root: Optional[TreeNode]) -> int:

        def solve(node):
            if node is None :
                return 0 
                
            leftHight = solve(node.left)
            rightHight = solve(node.right)

            return max(leftHight,rightHight) + 1

        return solve(root)