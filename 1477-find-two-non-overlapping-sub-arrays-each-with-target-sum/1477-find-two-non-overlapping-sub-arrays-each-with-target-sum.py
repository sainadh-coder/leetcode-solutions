class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        best = [float('inf')] * n
        seen = {0: -1}
        total = 0
        min_len = float('inf')
        ans = float('inf')

        for i, x in enumerate(arr):
            total += x

            if total - target in seen:
                j = seen[total - target]
                length = i - j

                if j >= 0 and best[j] != float('inf'):
                    ans = min(ans, length + best[j])

                min_len = min(min_len, length)

            best[i] = min(min_len, best[i - 1] if i > 0 else float('inf'))
            seen[total] = i

        return ans if ans != float('inf') else -1