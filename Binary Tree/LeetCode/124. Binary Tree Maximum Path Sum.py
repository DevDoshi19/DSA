# Definition for a binary tree node.

from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        self.maxi = float("-inf")
        
        def dfs(node):
            if not node :
                return 0

            LH = max(dfs(node.left),0)
            RH = max(dfs(node.right),0)
        
            self.maxi = max(self.maxi,LH+node.val+RH)

            return node.val + max(LH,RH)

        dfs(root)
        return self.maxi