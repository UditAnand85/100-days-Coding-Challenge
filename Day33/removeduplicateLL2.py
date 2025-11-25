# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def deleteDuplicates(self, head):
        if head is None or head.next is None:
            return head

        temp = head
        prev = None

       
        while temp != None:
            duplicate = False

          
            while temp.next != None and temp.val == temp.next.val:
                duplicate = True
                temp = temp.next      

            if duplicate:
              
                if prev == None:
                    head = temp.next
                else:
                    prev.next = temp.next
            else:
        
                prev = temp

            temp = temp.next

        return head
        