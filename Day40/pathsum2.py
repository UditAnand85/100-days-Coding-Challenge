# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root, targetSum):
        ans = []

        def dfs(node, cur_sum, path):
            if not node:
                return

            path.append(node.val)
            cur_sum += node.val

        
            if not node.left and not node.right:
                if cur_sum == targetSum:
                    ans.append(list(path))

            dfs(node.left, cur_sum, path)
            dfs(node.right, cur_sum, path)

            path.pop()  

        dfs(root, 0, [])
        return ans
