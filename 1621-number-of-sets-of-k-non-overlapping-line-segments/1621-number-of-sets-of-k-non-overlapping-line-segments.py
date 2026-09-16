class Solution:
    def numberOfSets(self, n: int, k: int) -> int:
        MOD = 10**9 + 7
        total = n + k - 1

        fact = [1] * (total + 1)
        for i in range(1, total + 1):
            fact[i] = fact[i - 1] * i % MOD

        def comb(a, b):
            return fact[a] * pow(fact[b], MOD - 2, MOD) % MOD * pow(fact[a - b], MOD - 2, MOD) % MOD

        return comb(total, 2 * k)