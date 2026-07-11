from typing import List, Optional


class TreeNode:
    def __init__(self):
        self.data = None
        self.left = None
        self.right = None


class Solution:
    def inorderTraversal(self,root:Optional[TreeNode]) -> List[int]:
        result = []
        current = root 

        while current is not None :
            if current.left is None :
                result.append(current.val)
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
                    result.append(current.data)

                    current = current.right

        return result