from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]: 

        if not root:
            return TreeNode(val)

        if val < root.val :
            root.left = self.insertIntoBST(root.left,val)
        if val > root.val :
            root.right = self.insertIntoBST(root.right,val)

        return root
    
# t.c. = O(h) where h is the height of the tree
# or in avg case it is O(log n) and in worst case it is O(n
# s.c. = O(h) where h is the height of the tree due to recursive stack space

class Solution1:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]: 

        if not root:
            return TreeNode(val)

        curr = root 
        while curr :
            if val < curr.val :
                if curr.left is None :
                    curr.left = TreeNode(val)
                    break
                else :
                    curr = curr.left 
            else :
                if curr.right is None :
                    curr.right = TreeNode(val)
                    break
                else :
                    curr = curr.right 

        return root