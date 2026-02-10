#Python3 Code
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        res = []
        while head:
            res.append(head.val)
            head = head.next
        
        res = sorted(res, reverse = True)
        #print(res)
        dummy = None
        
        for node in res:
            head = ListNode(node)
            head.next = dummy
            dummy = head
            
        return dummy
            