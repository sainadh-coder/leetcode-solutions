class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        freq = {'a':0,'b':0,'c':0}
        l = 0
        ans = 0
        n = len(s)

        for r in range(n):
            freq[s[r]] += 1

            while freq['a'] > 0 and freq['b'] > 0 and freq['c'] > 0:
                ans += n - r
                freq[s[l]] -= 1
                l += 1

        return ans