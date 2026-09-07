class Solution:
    def distinctSubseqII(self, s: str) -> int:
        MOD = 10**9 + 7
        n = len(s)

        dp = [0] * (n + 1)
        dp[0] = 1

        last = {}

        for i in range(1, n + 1):
            ch = s[i - 1]

            # Take current character
            dp[i] = (2 * dp[i - 1]) % MOD

            # Remove duplicate subsequences
            if ch in last:
                dp[i] -= dp[last[ch] - 1]
                dp[i] %= MOD

            last[ch] = i

        return (dp[n] - 1) % MOD