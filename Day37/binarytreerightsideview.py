# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root):
        if not root:
            return []

        q = [root]
        ans = []

        while q:
            size = len(q)
            for i in range(size):
                node = q.pop(0)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

                if i == size - 1:  
                    ans.append(node.val)

        return ans

        