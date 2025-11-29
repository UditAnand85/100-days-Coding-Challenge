'''
class Node:
    def __init__(self, val):
        self.data = val
        self.left = None
        self.right = None
'''

from collections import deque

class Solution:
    def topView(self, root):
        if not root:
            return []

        q = deque()
        q.append((root, 0))  

        hd_map = {}     

        min_hd = max_hd = 0

        while q:
            node, hd = q.popleft()

            if hd not in hd_map:          
                hd_map[hd] = node.data

            min_hd = min(min_hd, hd)
            max_hd = max(max_hd, hd)

            if node.left:
                q.append((node.left, hd - 1))
            if node.right:
                q.append((node.right, hd + 1))

        ans = []
        for hd in range(min_hd, max_hd + 1):
            ans.append(hd_map[hd])

        return ans

        
        