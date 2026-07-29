from collections import Counter

class Solution:
    def __init__(self):
        self.MAX = 10**6 + 1

    def smallestPalindrome(self, s: str, k: int) -> str:
        count = Counter(s)

        half = [0] * 26
        mid = ""

        for ch, freq in count.items():
            half[ord(ch) - ord("a")] = freq // 2
            if freq % 2:
                mid = ch

        total = self.countWays(half)
        if k > total:
            return ""

        left = []
        m = sum(half)

        for _ in range(m):
            for i in range(26):
                if half[i] == 0:
                    continue

                half[i] -= 1
                ways = self.countWays(half)

                if ways >= k:
                    left.append(chr(i + ord("a")))
                    break

                k -= ways
                half[i] += 1

        left = "".join(left)
        return left + mid + left[::-1]

    def countWays(self, cnt):
        total = sum(cnt)
        ans = 1

        for x in cnt:
            ans *= self.nCr(total, x)
            if ans >= self.MAX:
                return self.MAX
            total -= x

        return ans

    def nCr(self, n, r):
        ans = 1

        for i in range(1, min(r, n - r) + 1):
            ans = ans * (n - i + 1) // i
            if ans >= self.MAX:
                return self.MAX

        return ans