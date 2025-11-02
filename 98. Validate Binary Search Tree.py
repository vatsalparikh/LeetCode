# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        return self.recurse(root, float('inf'), float('-inf'))

    def recurse(self, root, upper, lower):
        if not root:
            return True

        if not lower < root.val < upper:
            return False

        left = self.recurse(root.left, root.val, lower)
        right = self.recurse(root.right, upper, root.val)

        return left and right