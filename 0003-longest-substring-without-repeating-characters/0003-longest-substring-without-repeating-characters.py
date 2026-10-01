class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ans = 0
        for i in range(len(s)):
            p = ""
            for j in range(i, len(s)):
                if s[j] in p:
                    break
                else:
                    p += s[j]
            ans = max(ans, len(p))
        return ans