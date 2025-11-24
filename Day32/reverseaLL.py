# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def reverseList(self, head):
        prev = None
        curr = head

        while curr:
            nxt = curr.next      # store next node
            curr.next = prev     # reverse pointer
            prev = curr          # move prev
            curr = nxt           # move curr

        return prev

        