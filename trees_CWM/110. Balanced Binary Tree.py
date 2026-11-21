# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        def dfs(node):
            if not node :
                return 0

            lh = dfs(node.left)
            rh = dfs(node.right)

            if lh is False or rh is False:
                return False
            if abs(lh-rh) > 1:
                return False

            return max(lh,rh) +1

        return dfs(root) is not False 