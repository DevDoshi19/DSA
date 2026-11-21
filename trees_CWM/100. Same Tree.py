# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def isSameTree(self, p: TreeNode | None, q: TreeNode | None) -> bool:
        def dfs(p,q):
            if not p and not q :
                return True
            if not p or not q :
                return False
            if p.val != q.val:
                return False

            if not dfs(p.left,q.left):
                return False

            if not dfs(p.right,q.right):
                return False
            return True

        return dfs(p,q)
