'''
class Node:
    def __init__(self, val):
        self.data = val
        self.right = None
        self.left = None
'''

class Solution:
    def boundaryTraversal(self, root):
        if not root:
            return []

        def isLeaf(node):
            return node.left is None and node.right is None

        def addLeft(node):
            while node:
                if not isLeaf(node):
                    left_boundary.append(node.data)
                node = node.left if node.left else node.right

        def addRight(node):
            temp = []
            while node:
                if not isLeaf(node):
                    temp.append(node.data)
                node = node.right if node.right else node.left
            right_boundary.extend(temp[::-1])

        def addLeaves(node):
            if not node:
                return
            if isLeaf(node):
                leaves.append(node.data)
            addLeaves(node.left)
            addLeaves(node.right)

        if isLeaf(root):
            return [root.data]

        left_boundary = [root.data]
        right_boundary = []
        leaves = []

        addLeft(root.left)
        addLeaves(root)
        addRight(root.right)

        return left_boundary + leaves + right_boundary
