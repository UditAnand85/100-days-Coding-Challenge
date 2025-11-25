# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        length = 0
        temp = head
        while temp:
            length += 1
            temp = temp.next

        
        if n == length:
            return head.next

        
        temp = head
        for _ in range(length - n - 1):
            temp = temp.next

      
        temp.next = temp.next.next

        return head



        