# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        self.maxi = float("-inf")
        def dfs(node):
            if not node :
                return 0 
            
            left = max(dfs(node.left),0)
            right = max(dfs(node.right),0)

            self.maxi = max(self.maxi,node.val+left+right)

            return node.val+max(left,right)

        dfs(root)
        return self.maxi
