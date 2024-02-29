# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        current = root

        while current:
            if current.val > q.val and current.val > p.val:
                current = current.left
            elif current.val < q.val and current.val < p.val:
                current = current.right
            else:
                return current
        