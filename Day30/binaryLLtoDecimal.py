# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def getDecimalValue(self, head):
        num = ""
        sum1 = 0
        while head != None:
            num = num + str(head.val)
            head = head.next

        for i in range(0,len(num)):
            sum1 = sum1 + (int(num[i]) * (2 ** (len(num)-(i+1))))
            
        return sum1