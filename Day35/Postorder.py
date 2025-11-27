# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def postorderTraversal(self, root):
        result = []

        def solve(node):
            if node is None:
                return
            solve(node.left)
            solve(node.right)
            result.append(node.val)

        solve(root)
        return result
        