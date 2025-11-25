# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head is None:
            return head

        list1 = []
        temp = head
        prev = None

        while temp != None:
            if temp.val in list1:
                prev.next = temp.next    
            else:
                list1.append(temp.val)
                prev = temp             

            temp = temp.next

        return head
