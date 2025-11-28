# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def zigzagLevelOrder(self, root):
        if not root:
            return []

        q = [root]
        ans = []
        left_to_right = True

        while q:
            size = len(q)
            level = []

            for _ in range(size):
                node = q.pop(0)
                level.append(node.val)
                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            if left_to_right:
                ans.append(level)
            else:
                ans.append(level[::-1])

            left_to_right = not left_to_right

        return ans

        