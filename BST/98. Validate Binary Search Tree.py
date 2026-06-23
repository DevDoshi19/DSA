# https://leetcode.com/problems/validate-binary-search-tree/solutions/7207912/easiest-way-dry-run-with-diagrams-beginn-whbr

# Solution link is above 

# Definition for a binary tree node.
from BST.Morris_algorith_FOR_IO_PO_traversal import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:

        def validate(node, min_val, max_val):
            if not node:
                return True
            if not (min_val < node.val < max_val):
                return False
            
            return (validate(node.left, min_val, node.val) and
                    validate(node.right, node.val, max_val))
        
        return validate(root, float('-inf'), float('inf'))

# Another solution is to do an inorder traversal and check if the elements are in sorted order or not. If they are not in sorted order then we can return false. This solution takes O(n) time complexity and O(n) space complexity in worst case when the tree is skewed. In average case it takes O(h) time complexity and O(h) space complexity where h is the height of the tree.

class Solution1:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        res =  []

        def DFS(node):
            if not node:
                return True

            if not DFS(node.left) :
                return False
            if len(res) > 0 and res[-1] >= node.val :
                return False
            res.append(node.val)
            
            return DFS(node.right) 

        return DFS(root)
    

# or first we just add in res then use for loop to check if the elements are in sorted order or not. This solution takes O(n) time complexity and O(n) space complexity in worst case when the tree is skewed. In average case it takes O(h) time complexity and O(h) space complexity where h is the height of the tree. 