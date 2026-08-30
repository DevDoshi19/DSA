# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:

        MOD = 10**9 + 7

        def total_sum(node):
            if not node:
                return 0
            return node.val + total_sum(node.left) + total_sum(node.right)

        self.total = total_sum(root)
        self.maxi = 0

        def dfs(node):
            if not node:
                return 0

            left_sum = dfs(node.left)
            right_sum = dfs(node.right)
            subtree_sum = left_sum + right_sum + node.val

            remaining = self.total - subtree_sum
            self.maxi = max(self.maxi, remaining * subtree_sum)

            return subtree_sum

        dfs(root)
        return self.maxi % MOD