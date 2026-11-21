from ast import List
from collections import deque
from typing import Optional
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        ans = []
        queue = deque()
        queue.append(root)
        while queue :
            level_order = len(queue)
            for i in range(level_order):
                node = queue.popleft()
                if i == level_order-1 :
                    ans.append(node.val)
                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
            
                 
        return ans
        