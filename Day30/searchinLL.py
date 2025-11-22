'''
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''

class Solution:
    def searchKey(self, head, key):

        if head.next == None and head != None:
            if head.data == key:
                return True

        while(head.next != None):
            if head.data == key:
                return True
            head = head.next
        if head.data == key:
            return True
        return False