# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        result = 0

        def dfs(root):
            nonlocal result
            value = [root.val]

            if root.left:
                value.extend(dfs(root.left))
            if root.right:
                value.extend(dfs(root.right))

            minv , maxv =  min(value), max(value)

            result = max(result, abs(root.val - minv), abs(root.val - maxv))
            return  minv , maxv
        dfs(root)
        return result
            

        
        