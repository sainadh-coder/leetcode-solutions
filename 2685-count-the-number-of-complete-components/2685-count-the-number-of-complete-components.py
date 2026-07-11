from collections import deque
from typing import List

class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        adj = [[] for _ in range(n)]

        for u, v in edges:
            adj[u].append(v)
            adj[v].append(u)

        visited = [False] * n
        ans = 0

        for i in range(n):
            if visited[i]:
                continue

            q = deque([i])
            visited[i] = True

            nodes = 0
            degree_sum = 0

            while q:
                u = q.popleft()
                nodes += 1
                degree_sum += len(adj[u])

                for v in adj[u]:
                    if not visited[v]:
                        visited[v] = True
                        q.append(v)

            edge_count = degree_sum // 2
            required = nodes * (nodes - 1) // 2

            if edge_count == required:
                ans += 1

        return ans