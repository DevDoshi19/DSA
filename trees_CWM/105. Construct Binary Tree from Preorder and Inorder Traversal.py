# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder or not inorder:
            return None

        root = TreeNode(preorder[0])
        mid = inorder.index(preorder[0])
        
        root.left = self.buildTree(preorder[1:mid+1],inorder[0:mid])
        root.right = self.buildTree(preorder[mid+1:],inorder[mid+1:])

        return root
    
class Solution2:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:

        inorder_map = {val: i for i, val in enumerate(inorder)}
        pre_idx = 0

        def dfs(left, right):
            nonlocal pre_idx

            if left > right:
                return None

            root_val = preorder[pre_idx]
            pre_idx += 1

            root = TreeNode(root_val)

            mid = inorder_map[root_val]

            root.left = dfs(left, mid - 1)
            root.right = dfs(mid + 1, right)

            return root

        return dfs(0, len(inorder) - 1)