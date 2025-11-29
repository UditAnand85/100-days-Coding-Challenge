# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque

class Solution:
    def verticalTraversal(self, root):
        if not root:
            return []

        q = deque()
        q.append((root, 0, 0))   
        nodes = []             

        while q:
            node, row, col = q.popleft()
            nodes.append((col, row, node.val))

            if node.left:
                q.append((node.left, row + 1, col - 1))
            if node.right:
                q.append((node.right, row + 1, col + 1))

        # sort by col → row → value
        nodes.sort()

        ans = []
        prev_col = None
        temp = []

        for col, row, val in nodes:
            if col != prev_col:
                if temp:
                    ans.append(temp)
                temp = []
                prev_col = col
            temp.append(val)

        ans.append(temp)
        return ans

        