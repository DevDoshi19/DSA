# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

# this is a simple solution to find the lowest common ancestor of two nodes in a binary tree. The idea is to traverse the tree and check if the current node is equal to either of the two nodes we are looking for. If it is, we return that node. If not, we recursively check the left and right subtrees. If both left and right subtrees return non-null values, it means that the current node is the lowest common ancestor. If only one of them returns a non-null value, we return that value up the recursion stack. If both return null, we return null.
# t.c. is O(n), s.c is O(h)

class Solution:
    def solve(self,node,p,q):
        if node is None :
            return None
        if node == p or node == q:
            return node
        left = self.solve(node.left,p,q)
        right = self.solve(node.right,p,q)
        if left is None and right is None :
            return None
        elif left is None:
            return right
        elif right is None:
            return left
        return node 

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.solve(root,p,q)


class Solution2:

# A better approach is we know that in a binary search tree, the left subtree of a node contains only nodes with values less than the node's value, and the right subtree contains only nodes with values greater than the node's value. So we can traverse the tree starting from the root and check if both p and q are less than the current node's value, then we move to the left subtree. If both p and q are greater than the current node's value, we move to the right subtree. If one of them is less and the other is greater, then we have found our lowest common ancestor.
# t.c. is O(h), s.c is O(1)

    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        curr = root 
        while curr :
            if p.val < curr.val and q.val < curr.val :
                curr = curr.left
            elif p.val > curr.val and q.val > curr.val:
                curr = curr.right
            else :
                return curr  
            
# 4 possible case :
# 1 . p and q are both in the left subtree of the current node, so we move to the left subtree.
# 2 . p and q are both in the right subtree of the current node, so we move to the right subtree.
# 3 . p is in the left subtree and q is in the right subtree of the current node, so we have found our lowest common ancestor.
# 4 . p is the current node or q is the current node, so we have found our lowest common ancestor.