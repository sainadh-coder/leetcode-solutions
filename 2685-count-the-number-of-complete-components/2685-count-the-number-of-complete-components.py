from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n

        def dfs(node):
            visited[node] = True
            nodes = 1
            degree_sum = len(adj[node])

            for nei in adj[node]:
                if not visited[nei]:
                    cnt, deg = dfs(nei)
                    nodes += cnt
                    degree_sum += deg

            return nodes, degree_sum

        ans = 0

        for i in range(n):
            if not visited[i]:
                nodes, degree_sum = dfs(i)
                edge_count = degree_sum // 2

                if edge_count == nodes * (nodes - 1) // 2:
                    ans += 1

        return ans