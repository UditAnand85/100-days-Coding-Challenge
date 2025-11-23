# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def middleNode(self, head):
        n=0
        temp = head
        while temp != None:
            n=n+1
            temp= temp.next
        mid = n // 2
        for i in range(mid):
            head= head.next

        return head
        