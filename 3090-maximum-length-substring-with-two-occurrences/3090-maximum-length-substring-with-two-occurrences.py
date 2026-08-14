class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            count = {}
            for j in range(i, len(s)):
                count[s[j]] = count.get(s[j], 0) + 1
                if count[s[j]] > 2:
                    break
                ans = max(ans, j - i + 1)
        return ans