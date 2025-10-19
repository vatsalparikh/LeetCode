# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    diameter = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.maxHeight(root)
        return self.diameter

    def maxHeight(self, root):
        if not root:
            return 0
        
        left_max = self.maxHeight(root.left)
        right_max = self.maxHeight(root.right)
        self.diameter = max(self.diameter, left_max + right_max)

        return 1 + max(left_max, right_max)