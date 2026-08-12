class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.diameter = 0
        self.maxHeight(root)
        return self.diameter

    def maxHeight(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        left = self.maxHeight(root.left)
        right = self.maxHeight(root.right)
        self.diameter = max(self.diameter, left + right)
        return 1 + max(left, right)