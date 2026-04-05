# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode], depth: int = 0) -> int:
        if not root:
            return 0
        
        if root and not root.left and not root.right:
            return depth + 1
        
        left_depth = self.maxDepth(root.left, depth + 1)
        right_depth = self.maxDepth(root.right, depth + 1)

        return max(left_depth, right_depth)