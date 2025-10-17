# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        return self.preorder(root, output)

    def preorder(self, root, output):
        if root:
            output.append(root.val)
            self.preorder(root.left, output)
            self.preorder(root.right, output)

        return output