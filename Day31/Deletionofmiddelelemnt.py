# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteMiddle(self, head):
        n=0
        temp = head
        while temp != None:
            n=n+1
            temp= temp.next
        mid = n // 2
        if mid == 0:
            return None
        temp2 = head

        for i in range(mid-1):
            temp2 = temp2.next
        temp2.next = temp2.next.next
        return head
        