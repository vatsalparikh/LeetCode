# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        output = []
        return self.inorder(root, output)

    def inorder(self, root, output) -> List[int]:
        if root:
            self.inorder(root.left, output)
            output.append(root.val)
            self.inorder(root.right, output)

        return output

