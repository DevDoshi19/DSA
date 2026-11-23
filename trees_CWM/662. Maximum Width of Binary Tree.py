# Definition for a binary tree node.
from collections import deque


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:

        if not root:
            return 0

        queue = deque()
        queue.append((root, 0))
        max_width = 0

        while queue:
            length = len(queue)

            first_index = queue[0][1]
            last_index = 0

            for i in range(length):
                node, index = queue.popleft()

                index -= first_index
                last_index = index

                if node.left:
                    queue.append((node.left, 2 * index))

                if node.right:
                    queue.append((node.right, 2 * index + 1))

            max_width = max(max_width, last_index + 1)

        return max_width

"""
Metric	Complexity
Time	O(N)
Auxiliary space	O(W)
Worst-case space	O(N)
"""
# dfs approach 
class Solution2:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        if not root:
            return 0

        leftmost = {}
        max_width = 0

        def dfs(node, depth, index):
            nonlocal max_width

            if not node:
                return

            if depth not in leftmost:
                leftmost[depth] = index

            width = index - leftmost[depth] + 1
            max_width = max(max_width, width)

            dfs(node.left, depth + 1, 2 * index)
            dfs(node.right, depth + 1, 2 * index + 1)

        dfs(root, 0, 0)

        return max_width