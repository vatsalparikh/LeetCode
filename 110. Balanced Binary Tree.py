# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        is_balanced, depth = self.recursiveDepth(root)
        return is_balanced

    def recursiveDepth(self, root):
        if not root:
            return (True, 0)

        is_left_balanced, left_depth = self.recursiveDepth(root.left)
        is_right_balanced, right_depth = self.recursiveDepth(root.right)

        if not is_left_balanced or not is_right_balanced or abs(left_depth - right_depth) > 1:
            return (False, 1 + max(left_depth, right_depth))

        return (True, 1 + max(left_depth, right_depth))

'''
        1
            2
                3
'''

        


        