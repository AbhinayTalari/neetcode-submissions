class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        res = -float('inf')
        def dfs(root):
            nonlocal res
            if not root:
                return 0
            left = max(0, dfs(root.left))
            right = max(0, dfs(root.right))
            res = max(res, root.val + left + right)
            return root.val + max(left, right)
        dfs(root)
        return res