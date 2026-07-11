# Definition for a binary tree node.
from typing import Optional


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# brute force solution is to do a dfs and store all the values in a list and then sort the list and return the kth smallest element. This solution takes O(nlogn) time complexity and O(n) space complexity.

# t.c. = O(n) + O(nlogn) = O(nlogn) , s.c. = O(n) stack space + O(n) result  = O(n)
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(node):
            if node is None:
                return  

            res.append(node.val)
            dfs(node.left)
            dfs(node.right)

        dfs(root)

        if len(res) < k :
            return None

        res.sort()

        return res[k-1]
    

# Better soltion 
# we have BST so we can just do an inorder traversal and just check that we have element the leangth of k , if yes then we can simple return adn cut down 
class Solution1:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        res = []

        def dfs(node):
            if node is None:
                return  

            dfs(node.left)
            res.append(node.val)
            if len(res) == k :
                return 
            dfs(node.right)

        dfs(root)

        if len(res) < k :
            return None

        return res[k-1]
    
"""
Note in inorder we always get the sorted order of the elements in the BST so we can just do an inorder traversal and just check that we have element the leangth of k , if yes then we can simple return adn cut down the traversal. This solution takes O(n) time complexity and O(n) space complexity in worst case when the tree is skewed. In average case it takes O(k) time complexity and O(k) space complexity.
"""


# soltion 3 :

class Solution3:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        self.count = 0
        self.res = 0
        def inorder(node):
            if node is None: 
                return 
            
            inorder(node.left)
            self.count +=1
            if self.count == k :
                self.res = node.val
                return
            inorder(node.right)

        inorder(root)
        return self.res
    
# simple logic is that we are doing an inorder traversal and we are keeping track of the count of the nodes we have visited and when the count is equal to k we return the value of the node. This solution takes O(n) time complexity and O(h) space complexity where h is the height of the tree. In average case it takes O(k) time complexity and O(h) space complexity.

# solution 4 : Morris Traversal

class Solution4:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        count = 0
        current = root 

        while current is not None :
            if current.left is None :
                count +=1
                if count == k :
                    return current.val
                current = current.right
            
            # current has left child 
            else:
                predecessor = current.left

                while (predecessor.right) is not None and predecessor.right != current:
                    predecessor = predecessor.right

                # make current as right child of predecesser

                if predecessor.right is None :
                    predecessor.right = current
                    current = current.left

                else :
                    # revert the changes 
                    predecessor.right = None 
                    count +=1
                    if count == k :
                        return current.val
                    current = current.right

        return -1