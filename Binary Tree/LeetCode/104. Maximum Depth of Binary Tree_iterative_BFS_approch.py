# Definition for a binary tree node.
from typing import Optional
from collections import deque

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        # Guard clause for empty trees
        if root is None:
            return 0
            
        height = 0 
        queue = deque([root]) # Can initialize directly with root

        while len(queue) != 0:
            level_size = len(queue)
            height += 1 

            for _ in range(level_size):
                e = queue.popleft()
                if e.left is not None:
                    queue.append(e.left)
                if e.right is not None:
                    queue.append(e.right)
                    
        return height
