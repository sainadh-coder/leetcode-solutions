from typing import List

class Solution:
    def pathExistenceQueries(
        self,
        n: int,
        nums: List[int],
        maxDiff: int,
        queries: List[List[int]]
    ) -> List[int]:

        arr = sorted((nums[i], i) for i in range(n))

        pos = [0] * n
        for i, (_, idx) in enumerate(arr):
            pos[idx] = i

        nxt = [0] * n

        r = 0
        for l in range(n):
            while r + 1 < n and arr[r + 1][0] - arr[l][0] <= maxDiff:
                r += 1
            nxt[l] = r

        LOG = n.bit_length()

        up = [[0] * n for _ in range(LOG)]
        up[0] = nxt[:]

        for k in range(1, LOG):
            for i in range(n):
                up[k][i] = up[k - 1][up[k - 1][i]]

        ans = []

        for u, v in queries:
            u = pos[u]
            v = pos[v]

            if u > v:
                u, v = v, u

            if u == v:
                ans.append(0)
                continue

            cur = u
            jumps = 0

            for k in range(LOG - 1, -1, -1):
                if up[k][cur] < v:
                    jumps += 1 << k
                    cur = up[k][cur]

            if up[0][cur] < v:
                ans.append(-1)
            else:
                ans.append(jumps + 1)

        return ans