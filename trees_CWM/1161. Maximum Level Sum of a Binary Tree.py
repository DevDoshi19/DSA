# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def maxLevelSum(self, root: TreeNode | None) -> int:
        if not root:
            return []

        queue = deque()
        queue.append(root)
        max_level = 0
        maxi = float("-inf")
        curr_level = 0 
        while queue:
            level = len(queue) 
            curr_level += 1
            curr_sum = 0 
            for i in range(level):
                node = queue.popleft()
                if node.left :
                    queue.append(node.left)
                if node.right :
                    queue.append(node.right)
                
                curr_sum += node.val
            
            if maxi < curr_sum :
                max_level = curr_level
                maxi = curr_sum
            
        return max_level
