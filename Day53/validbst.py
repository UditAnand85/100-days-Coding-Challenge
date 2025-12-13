# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isValidBST(self, root):
        prev = [None]

        def inorder(node):
            if not node:
                return True
            if not inorder(node.left):
                return False
            if prev[0] is not None and node.val <= prev[0]:
                return False
            prev[0] = node.val
            return inorder(node.right)

        return inorder(root)