'''
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
'''

class Solution:
    def findPreSuc(self, root, key):
        predecessor = None
        successor = None
        curr = root

        while curr:
            if key < curr.data:
                successor = curr
                curr = curr.left
            elif key > curr.data:
                predecessor = curr
                curr = curr.right
            else:
                break

        if curr and curr.left:
            temp = curr.left
            while temp.right:
                temp = temp.right
            predecessor = temp
            
        if curr and curr.right:
            temp = curr.right
            while temp.left:
                temp = temp.left
            successor = temp

        return predecessor, successor