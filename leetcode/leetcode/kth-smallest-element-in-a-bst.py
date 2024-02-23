# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:

        def inorder(node,arr):
            if not node:
                return None

            inorder(node.left,arr)
            arr.append(node.val)
            inorder(node.right,arr)

        arr = []
        inorder(root,arr)

        return arr[k-1]

        # n = 0
        # stack = []
        # current = root
    
        # while current:
        #     while current:
        #         stack.append(current.val)
        #         current = current.left
        #     # so at the moment we get the current.left null we pop from our stack
        #     print(stack)
        #     if stack:
        #         curr = stack.pop()
        #         n+=1
            
        #     if n == k:
        #         return curr
        #     current =  current.right

        # return 1
        