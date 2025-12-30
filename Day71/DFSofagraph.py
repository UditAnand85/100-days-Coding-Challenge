class Solution:
    def dfs(self, adj):
        V = len(adj)                 
        visited = [False] * V
        res = []

        def dfs(node):
            visited[node] = True
            res.append(node)
            for nei in adj[node]:   
                if not visited[nei]:
                    dfs(nei)

        dfs(0)                      
        return res