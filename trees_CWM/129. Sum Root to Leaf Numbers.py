# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        if not root :
            return 0

        self.sum = 0
        def dfs(node,num):
            num = num * 10 + node.val
            if not node.left and not node.right :
                self.sum += int(num)
                return 

            if node.left:
                dfs(node.left,num)
            if node.right:
                dfs(node.right,num)

        dfs(root,0)
        return self.sum