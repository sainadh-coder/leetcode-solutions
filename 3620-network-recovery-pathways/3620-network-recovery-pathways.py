from heapq import heappush, heappop
from math import inf

class Solution:
    def findMaxPathScore(self, edges, online, k):
        n = len(online)

        g = [[] for _ in range(n)]

        mn = inf
        mx = 0

        for u, v, w in edges:
            if not online[u] or not online[v]:
                continue

            g[u].append((v, w))
            mn = min(mn, w)
            mx = max(mx, w)

        if mn == inf:
            return -1

        def check(mid):
            dist = [inf] * n
            dist[0] = 0

            pq = [(0, 0)]

            while pq:
                d, u = heappop(pq)

                if d > dist[u]:
                    continue

                if d > k:
                    continue

                if u == n - 1:
                    return True

                for v, w in g[u]:
                    if w < mid:
                        continue

                    nd = d + w

                    if nd < dist[v]:
                        dist[v] = nd
                        heappush(pq, (nd, v))

            return False

        l, r = 0, mx

        while l < r:
            mid = (l + r + 1) // 2

            if check(mid):
                l = mid
            else:
                r = mid - 1

        return l if check(l) else -1