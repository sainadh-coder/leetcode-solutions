from typing import List
from bisect import bisect_right

class Solution:
    def gcdValues(self, nums: List[int], queries: List[int]) -> List[int]:
        mx = max(nums)

        freq = [0] * (mx + 1)
        for x in nums:
            freq[x] += 1

        cnt = [0] * (mx + 1)

        for d in range(1, mx + 1):
            for m in range(d, mx + 1, d):
                cnt[d] += freq[m]

        exact = [0] * (mx + 1)

        for d in range(mx, 0, -1):
            exact[d] = cnt[d] * (cnt[d] - 1) // 2

            for m in range(2 * d, mx + 1, d):
                exact[d] -= exact[m]

        pref = [0] * (mx + 1)

        for d in range(1, mx + 1):
            pref[d] = pref[d - 1] + exact[d]

        ans = []

        for q in queries:
            ans.append(bisect_right(pref, q))

        return ans