from typing import List
from bisect import bisect_left

class Solution:
    def maximumWeight(self, intervals: List[List[int]]) -> List[int]:
        n = len(intervals)

        arr = []
        for i in range(n):
            arr.append((intervals[i][1], intervals[i][0], intervals[i][2], i))

        arr.sort()

        ends = [x[0] for x in arr]

        prev = [0] * n

        for i in range(n):
            start = arr[i][1]
            prev[i] = bisect_left(ends, start, 0, i)

        dp = [[(0, ()) for _ in range(5)] for _ in range(n + 1)]

        for i in range(1, n + 1):
            end, start, weight, idx = arr[i - 1]

            for cnt in range(5):
                dp[i][cnt] = dp[i - 1][cnt]

                if cnt > 0:
                    p = prev[i - 1]

                    old_weight, old_indices = dp[p][cnt - 1]

                    new_weight = old_weight + weight
                    new_indices = tuple(sorted(old_indices + (idx,)))

                    if new_weight > dp[i][cnt][0]:
                        dp[i][cnt] = (new_weight, new_indices)

                    elif new_weight == dp[i][cnt][0]:
                        if new_indices < dp[i][cnt][1]:
                            dp[i][cnt] = (new_weight, new_indices)

        best = (0, ())

        for cnt in range(1, 5):
            if dp[n][cnt][0] > best[0]:
                best = dp[n][cnt]

            elif dp[n][cnt][0] == best[0]:
                if dp[n][cnt][1] < best[1]:
                    best = dp[n][cnt]

        return list(best[1])