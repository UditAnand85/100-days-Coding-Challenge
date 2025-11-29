'''
# Node Class:
class Node:
    def _init_(self,val):
        self.data = val
        self.left = None
        self.right = None
'''
#Complete the function below
from collections import deque

class Solution:
    def diagonal(self, root):
        if not root:
            return []

        q = deque()
        q.append(root)

        ans = []

        while q:
            node = q.popleft()

            
            while node:
                ans.append(node.data)

                if node.left:
                    q.append(node.left) 

                node = node.right       

        return ans

