class Solution:
    def hasPathSum(self, root, targetSum):
        if not root:
            return False

        def dfs(node, total):
            total += node.val

            # Leaf node check
            if not node.left and not node.right:
                return total == targetSum  # ✅

            if node.left and dfs(node.left, total):
                return True
            if node.right and dfs(node.right, total):
                return True

            return False

        return dfs(root, 0)