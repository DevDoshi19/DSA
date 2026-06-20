# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        def solve(node):
            if node is None :
                return 0 

            leftheight = solve(node.left)
            rightheight = solve(node.right)
            self.diameter = max(self.diameter,leftheight+rightheight)
            return max(leftheight,rightheight) + 1

        solve(root)

        return self.diameter