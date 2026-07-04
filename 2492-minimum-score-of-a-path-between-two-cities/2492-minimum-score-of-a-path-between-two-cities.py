from collections import defaultdict, deque

class Solution:
    def minScore(self, n: int, roads: List[List[int]]) -> int:
        graph = defaultdict(list)

        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))

        q = deque([1])
        visited = {1}
        ans = float('inf')

        while q:
            node = q.popleft()

            for nei, weight in graph[node]:
                ans = min(ans, weight)

                if nei not in visited:
                    visited.add(nei)
                    q.append(nei)

        return ans