from typing import List ,Optional
from collections import deque
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        queue = deque()
        result = {}
        ans = []

        if root is None:
            return []

        queue.append((root,1))

        while len(queue) != 0 :
            e,level = queue.popleft()
            result[level] = e.val 

            if e.left :
                queue.append((e.left,level+1))

            if e.right:
                queue.append((e.right,level+1))
            
        for val in sorted(result.items()):
            ans.append(val[1])

        return ans 



# using DFS ... Postorder but reverse ( root -> right -> left)


class Solution1:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        ans = []
        
        def reversepostorder(node, level):
            if node is None:
                return 

            if level == len(ans):
                ans.append(node.val)
                
            reversepostorder(node.right, level + 1)
            reversepostorder(node.left, level + 1)

        if root is None:
            return []

        reversepostorder(root,0)

        return ans 
    

# What we are doing is we are first going to store right node , and then check that that level is store that's why we dont going to store that
# so we are go for next level 

# t.c. is O(N)
# s.c. is O(N)