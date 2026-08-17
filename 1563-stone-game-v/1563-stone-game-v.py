class Solution:
    def stoneGameV(self, stoneValue: List[int]) -> int:
        n = len(stoneValue)

        prefix = [0] * (n + 1)
        for i in range(n):
            prefix[i + 1] = prefix[i] + stoneValue[i]

        dp = [[0] * n for _ in range(n)]

        leftMax = [[0] * n for _ in range(n)]
        rightMax = [[0] * n for _ in range(n)]

        for i in range(n):
            leftMax[i][i] = stoneValue[i]
            rightMax[i][i] = -prefix[i]

        for length in range(2, n + 1):
            for l in range(n - length + 1):
                r = l + length - 1

                total = prefix[l] + prefix[r + 1]

                lo, hi = l, r - 1
                split = l - 1

                # Find last split where left <= right
                while lo <= hi:
                    mid = (lo + hi) // 2

                    if 2 * prefix[mid + 1] <= total:
                        split = mid
                        lo = mid + 1
                    else:
                        hi = mid - 1

                best = 0

                # left <= right
                if split >= l:
                    best = max(best, leftMax[l][split])

                # right side
                if split >= l and 2 * prefix[split + 1] == total:
                    start = split + 1
                else:
                    start = split + 2

                if start <= r:
                    best = max(best, rightMax[start][r] + prefix[r + 1])

                dp[l][r] = best

                leftMax[l][r] = max(
                    leftMax[l][r - 1],
                    dp[l][r] + prefix[r + 1] - prefix[l]
                )

                rightMax[l][r] = max(
                    rightMax[l + 1][r],
                    dp[l][r] - prefix[l]
                )

        return dp[0][n - 1]