# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        
        ctr = 0
        value = []
        counter = head
        while counter:
            counter = counter.next
            ctr+=1
        
        ctr-=1
        res = 0
        
        while head:
            res+=(int(head.val)*2**ctr)
            ctr-=1
            head = head.next
        return res
            
        
        
        
        