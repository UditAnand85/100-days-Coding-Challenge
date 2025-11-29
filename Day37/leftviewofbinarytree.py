class Solution:
    def leftView(self, root):
        if not root:
            return []

        q = [root]
        ans = []

        while q:
            size = len(q)
            for i in range(size):
                node = q.pop(0)

                if i == 0:          
                    ans.append(node.data)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

        return ans