# class Node:
#     def __init__(self):
#         self.data = None
#         self.left = None
#         self.right = None
        
class Solution:
    def absolute_diff(self,root):
        self.prev = None
        self.ans = float("inf")

        def inorder(node):
            if not node:
                return
            inorder(node.left)

            if self.prev is not None:
                self.ans = min(self.ans, node.data - self.prev)
            self.prev = node.data

            inorder(node.right)

        inorder(root)
        return self.ans