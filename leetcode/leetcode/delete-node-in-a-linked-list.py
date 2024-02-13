# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def deleteNode(self, node):
        while node:
            val=node.next.val
            node.val=val
            node.next=node.next.next
            break