from collections import deque
import heapq

class Solution:
    def maximumSafenessFactor(self, grid):
        n = len(grid)

        # Step 1: Distance from nearest thief
        dist = [[-1] * n for _ in range(n)]
        q = deque()

        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dist[i][j] = 0
                    q.append((i, j))

        dirs = [(1,0), (-1,0), (0,1), (0,-1)]

        while q:
            r, c = q.popleft()

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if 0 <= nr < n and 0 <= nc < n and dist[nr][nc] == -1:
                    dist[nr][nc] = dist[r][c] + 1
                    q.append((nr, nc))

        # Step 2: Dijkstra / Max Heap
        pq = [(-dist[0][0], 0, 0)]
        visited = {(0, 0)}

        while pq:
            safe, r, c = heapq.heappop(pq)
            safe = -safe

            if r == n - 1 and c == n - 1:
                return safe

            for dr, dc in dirs:
                nr, nc = r + dr, c + dc

                if (
                    0 <= nr < n and
                    0 <= nc < n and
                    (nr, nc) not in visited
                ):
                    visited.add((nr, nc))

                    new_safe = min(safe, dist[nr][nc])

                    heapq.heappush(
                        pq,
                        (-new_safe, nr, nc)
                    )

        return 0