class Solution:
    def bfs(self, adj):
        V = len(adj)
        visited = [False] * V
        res = []
    
        q = [0]          
        visited[0] = True
        idx = 0         
    
        while idx < len(q):
            node = q[idx]
            idx += 1
            res.append(node)
    
            for nei in adj[node]:   
                if not visited[nei]:
                    visited[nei] = True
                    q.append(nei)
    
        return res
