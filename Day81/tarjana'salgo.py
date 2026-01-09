class Solution:
    def tarjans(self, V, adj):
        disc = [-1] * V
        low = [-1] * V
        in_stack = [False] * V
        stack = []
        timer = 0
        sccs = []

        def dfs(u):
            nonlocal timer
            disc[u] = low[u] = timer
            timer += 1
            stack.append(u)
            in_stack[u] = True

            for v in adj[u]:
                if disc[v] == -1:
                    dfs(v)
                    low[u] = min(low[u], low[v])
                elif in_stack[v]:
                    low[u] = min(low[u], disc[v])

            # head of SCC
            if low[u] == disc[u]:
                scc = []
                while True:
                    node = stack.pop()
                    in_stack[node] = False
                    scc.append(node)
                    if node == u:
                        break
                sccs.append(sorted(scc))

        for i in range(V):
            if disc[i] == -1:
                dfs(i)

        # 🔑 sort SCCs by their smallest element (GFG requirement)
        sccs.sort(key=lambda x: x[0])

        return sccs
