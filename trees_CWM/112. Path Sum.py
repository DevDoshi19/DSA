# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode | None, targetSum: int) -> bool:
        if not root :
            return False

        def dfs(node,total):
            total += node.val
            if not node.left and not node.right :
                if total == targetSum :
                    return True
                return False
            
            # if total >= targetSum :
            #     return False

            if node.left and dfs(node.left,total) :
                return True
            if node.right and dfs(node.right,total):
                return True
            
            return False

        return dfs(root,0)