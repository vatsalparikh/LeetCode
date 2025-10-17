# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        return self.postorder(root, output)

    def postorder(self, root, output):
        if root:
            self.postorder(root.left, output)
            self.postorder(root.right, output)
            output.append(root.val)

        return output