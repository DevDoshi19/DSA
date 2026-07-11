# Definition for a binary tree node.
from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        
        def backtrack(node) :
            if not node or node.val == val :
                return node

            if val < node.val:
                return backtrack(node.left)

            if val > node.val :
                return backtrack(node.right)

        return backtrack(root) 

# Time Complexity : O(h) where h is the height of the tree
# Space Complexity : O(h) where h is the height of the tree

class Solution1:
    def searchBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        curr = root
        
        while curr:
            if curr.val == val:
                return curr  # Found the node, return it directly
            elif val < curr.val:
                curr = curr.left  # Go left
            else:
                curr = curr.right  # Go right
                
        return None  # Value not found
