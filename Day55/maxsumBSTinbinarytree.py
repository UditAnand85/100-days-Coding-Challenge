# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxSumBST(self, root):
        self.maxSum = 0

        def dfs(node):
            if not node:
                return True, 0, float('inf'), float('-inf')

            l_isBST, l_sum, l_min, l_max = dfs(node.left)
            r_isBST, r_sum, r_min, r_max = dfs(node.right)

            if l_isBST and r_isBST and l_max < node.val < r_min:
                curr_sum = l_sum + r_sum + node.val
                self.maxSum = max(self.maxSum, curr_sum)
                return True, curr_sum, min(l_min, node.val), max(r_max, node.val)

            return False, 0, 0, 0

        dfs(root)
        return self.maxSum
        