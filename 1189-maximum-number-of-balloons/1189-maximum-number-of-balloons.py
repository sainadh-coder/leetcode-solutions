class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        balloon_freq = {}
        for ch in set("balloon"):
            balloon_freq[ch] = "balloon".count(ch)
        text_freq = {}
        for ch in set(text):
            text_freq[ch] = text.count(ch)
        ans = float('inf')

        for ch in balloon_freq:
            if ch not in text_freq:
                return 0
            ans = min(ans, text_freq[ch] // balloon_freq[ch])
        return ans