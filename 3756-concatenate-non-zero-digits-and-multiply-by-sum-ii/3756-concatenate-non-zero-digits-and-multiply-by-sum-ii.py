from typing import List
from bisect import bisect_left, bisect_right

class Solution:
    def sumAndMultiply(self, s: str, queries: List[List[int]]) -> List[int]:
        MOD = 10**9 + 7

        pos = []
        digits = []

        for i, ch in enumerate(s):
            if ch != '0':
                pos.append(i)
                digits.append(int(ch))

        m = len(digits)

        # powers of 10
        pow10 = [1] * (m + 1)
        for i in range(1, m + 1):
            pow10[i] = (pow10[i - 1] * 10) % MOD

        # prefix concatenated value
        pref_num = [0] * (m + 1)
        for i in range(m):
            pref_num[i + 1] = (pref_num[i] * 10 + digits[i]) % MOD

        # prefix digit sums
        pref_sum = [0] * (m + 1)
        for i in range(m):
            pref_sum[i + 1] = pref_sum[i] + digits[i]

        ans = []

        for l, r in queries:

            L = bisect_left(pos, l)
            R = bisect_right(pos, r) - 1

            if L > R:
                ans.append(0)
                continue

            digit_sum = pref_sum[R + 1] - pref_sum[L]

            length = R - L + 1

            number = (
                pref_num[R + 1]
                - pref_num[L] * pow10[length]
            ) % MOD

            ans.append((number * digit_sum) % MOD)

        return ans