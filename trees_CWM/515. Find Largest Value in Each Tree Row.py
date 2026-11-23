# Definition for a binary tree node.
from collections import deque
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def largestValues(self, root: TreeNode | None) -> list[int]:
        if not root:
            return []

        ans = []
        queue = deque()
        queue.append(root)

        while queue :
            level = len(queue)
            maxi = float("-inf")
            for i in range(level):
                node = queue.popleft()
                if node.left :
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                
                maxi = max(maxi,node.val)

            ans.append(maxi)

        return ans