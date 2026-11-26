# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode | None:
        # recursive approach , t.c. = O(n) , s.c. = O(n) in worst case O(n**2) 
        if not preorder or not postorder:
            return None
        
        root = TreeNode(preorder[0])
        if len(preorder) == 1:
            return root

        index = postorder.index(preorder[1])
        left_size = index + 1

        root.left = self.constructFromPrePost(preorder[1:left_size + 1],postorder[:left_size])
        root.right = self.constructFromPrePost(preorder[left_size + 1:],postorder[left_size:-1])

        return root

class Solution2:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode | None:
        post_map = {val: i for i, val in enumerate(postorder)}

        def build(pre_start, pre_end, post_start, post_end):
            if pre_start > pre_end:
                return None

            root = TreeNode(preorder[pre_start])

            if pre_start == pre_end:
                return root

            left_root = preorder[pre_start + 1]
            left_root_index = post_map[left_root]

            left_size = left_root_index - post_start + 1

            root.left = build(
                pre_start + 1,
                pre_start + left_size,
                post_start,
                left_root_index
            )

            root.right = build(
                pre_start + left_size + 1,
                pre_end,
                left_root_index + 1,
                post_end - 1
            )

            return root

        return build(0, len(preorder) - 1, 0, len(postorder) - 1)