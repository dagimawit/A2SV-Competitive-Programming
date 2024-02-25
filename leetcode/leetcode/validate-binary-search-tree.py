# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode], min_val=float(-inf), max_val=float(inf)) -> bool:
        return False if root.val < min_val or root.val > max_val else ((not root.right or self.isValidBST(root.right, root.val + 1, max_val)) and (not root.left or self.isValidBST(root.left, min_val, root.val - 1 )))