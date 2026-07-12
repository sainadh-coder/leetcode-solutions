from itertools import accumulate

class Solution:
    def zigZagArrays(self, n: int, l: int, r: int) -> int:
        MOD = 10**9 + 7
        m = r - l + 1

        up = [m - 1 - i for i in range(m)]
        down = [i for i in range(m)]

        if n == 2:
            return (sum(up) + sum(down)) % MOD

        for _ in range(3, n + 1):
            pref_up = list(accumulate(up))
            pref_down = list(accumulate(down))

            total_down = pref_down[-1]

            new_down = [0] + [x % MOD for x in pref_up[:-1]]
            new_up = [(total_down - x) % MOD for x in pref_down]

            up = new_up
            down = new_down

        return (sum(up) + sum(down)) % MOD